import pandas as pd 
import numpy as np 
from sklearn import preprocessing 
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 

import keras 
import math 
import tensorflow as tf 

from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras import optimizers

#genererator
from keras.preprocessing.sequence import TimeseriesGenerator
import pandas_datareader as web

#  df =web.DataReader('^GSPC',data_source='yahoo',start='2020-01-05',end='2020-05-07')



class StockData:

    def __init__(self):

        #uncommnet if need 1998 -2020 data 
        # self.data = pd.read_csv('sp500.csv')

#we are using the stock data from pandas data reader library to extract data 
        self.data = web.DataReader('^GSPC',data_source='yahoo',start='2020-01-05',end='2020-05-07')
        self.history_data_pts = 60
        self.look_back = 15
        self.batch_size = 1
        self.scaler = MinMaxScaler(feature_range=(0,1))
        self.model = Sequential()

    def drop_date(self):

        self.data_no_date = self.data.drop('Date',axis=1)
        
        return self.data_no_date

    def normalize_data(self):

        data_no_date = StockData().drop_date()
        data_normalizer = preprocessing.MinMaxScaler()
        data_normalized = data_normalizer.fit_transform(data_no_date)

        return data_normalized


    
#splitting data this is for the deep learning portion whereby we have to split the data 
#into test and training data sets 
    def train_test_split_data(self):

        data_no_date = StockData().drop_date()
                #   Open         High          Low        Close    Adj Close     Volume

        X=data_no_date[['Open','High','Low','Volume']]
        y=data_no_date['Close']

        # print(data_no_date.head(5))

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

        return X_train, X_test,y_train ,y_test


# here we envoke the Timeseries generator from keras deep learning framework     
    def generate_time_sequence(self):
        pass 

        data_no_date = StockData().drop_date()

        dataset = self.scaler.fit_transform(data_no_date)

        # price_data = data_no_date['Close']

        train_size = math.floor(len(dataset)*0.7)

        test_size = math.floor(len(dataset)-train_size)

        train , test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]


        train_gen = TimeseriesGenerator(train,train,self.look_back,batch_size=1)
        test_gen = TimeseriesGenerator(test,test,self.look_back,batch_size=1)


        self.model.add(LSTM(10,activation='relu',input_shape=(self.look_back,1)))
        self.model.add(Dense(1))

        self.model.compile(optimizer='adam',loss='mse')

        history = model.fit(data["X_train"], data["y_train"],
                    batch_size=BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_data=(data["X_test"], data["y_test"]),
                    callbacks=[checkpointer, tensorboard],
                    verbose=1)


    def LSTM_model(self):

        #check that the data splits as an int 

        split_percent =0.8
        num_epochs = 8

        data_no_date = StockData().drop_date()

        close_price = data_no_date['Close'].values

        close_price = close_price.reshape((-1,1))

        split = int(split_percent*len(close_price))
        price_train = close_price[:split]
        price_test = close_price[split:]

        #check on batch size
        train_gen = TimeseriesGenerator(price_train,price_train,length=self.look_back,batch_size=1)
        test_gen = TimeseriesGenerator(price_test,price_test,length= self.look_back,batch_size=1)

        self.model.add(LSTM(10,activation='relu',input_shape=(self.look_back,1)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam',loss='mse')
        self.model.fit_generator(train_gen,epochs=num_epochs,verbose=1)


#this will allow for the prices to be calculated looking forward for futures dates 
    def predict_prices(self):

        num_prediction = 15


        data_no_date = StockData().drop_date()
        close_price = data_no_date['Close'].values

        close_price = close_price.reshape((-1))

        prediction_list = close_price[-self.look_back:]

        for i in range(num_prediction):

            x = prediction_list[-self.look_back:]
            x = x.reshape((1,self.look_back,1))

            out = self.model.predict(x)[0][0]

            prediction_list = np.append(prediction_list,out)


        prediction_list = prediction_list[self.look_back-1:]


        return prediction_list

    def get_dates(self):

        split_percent =0.8
        num_prediction = 15 

        date = self.data['Date']
        split = int(split_percent*len(date))

        date_train=date[:split]
        date_test=date[split:]

        last_date = date.values[-1]

        prediction_dates=pd.date_range(last_date,periods=num_prediction+1).tolist()


        return prediction_dates 
      

stock_data=StockData()

check_pred = stock_data().train_test_split_data()

print(check_pred)

# date=stock_data.get_dates()
# list_prices=stock_data.predict_prices()
# print(list_prices)


# print(date)
