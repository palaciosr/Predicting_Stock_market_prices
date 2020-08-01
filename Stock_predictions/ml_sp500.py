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



"""
This class grabs the stock data with the pandas_datareader library
It then uses Keras deep learning framework with long term short term memory
in order to predict the future stock prices for the next (future) five days.
The amount of historical data that is taken for this experiment is 60 days.

"""

class StockData:

    def __init__(self,stock):

        #uncomment  if you want the  date range from 1998-2020 
        # self.data = pd.read_csv('../data/sp500.csv')
        # self.data = web.DataReader(stock,data_source='yahoo',start='2020-04-05',end='2020-06-05')
        self.data = stock
        self.history_data_pts = 60
        self.look_back = 4
        self.batch_size = 1
        self.scaler = MinMaxScaler(feature_range=(0,1))
        self.model = Sequential()


    #Date was an index changing it into a column
    def check_stock_exisits(self):

        try:
            self.data 
            return True
        except KeyError:
            print("This input is not valid")
            return False


    def get_date(self):
         
        self.data=self.data.reset_index(level=['Date'])


        return self.data 

        

    #I want to normalize the data in order to get returns and prices 
    #I will include research which shows normal and log normal distributions
    # for returns and price fluctations 
    def normalize_data(self):
        

        data_no_date = StockData().drop_date()
        data_normalizer = preprocessing.MinMaxScaler()
        data_normalized = data_normalizer.fit_transform(data_no_date)

        return data_normalized


    
#splitting data this is for the deep learning portion whereby we have to split the data 
#into test and training data sets 
    def train_test_split_data(self):

        # data_no_date = StockData().drop_date()
        #columns are below         
        #Open,High ,Low ,Close, Adj Close,Volume

        X=self.data[['Open','High','Low','Volume']]
        y=self.data['Close']

        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

        return X_train, X_test,y_train ,y_test


# here we envoke the Timeseries generator from keras deep learning framework     
    def generate_time_sequence(self):
        pass 

        data_no_date = StockData().drop_date()

        dataset = self.scaler.fit_transform(data_no_date)

        train_size = math.floor(len(dataset)*0.7)

        test_size = math.floor(len(dataset)-train_size)

        #scaling the test and train data sets 
        train , test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

        #Time series generator takes the train and test and uses it to generate future data 
        #note that in its purest form the data generator is just generating data with 
        #random generator native to python 
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


        split_percent =0.8
        num_epochs = 8

        # data_no_date = StockData().drop_date()

        close_price = self.data['Close'].values

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
#note I am using the Close stock prices but there can be a variation of times to 
#do prediction on 
    def predict_prices(self):

        num_prediction = 4


        # data_no_date = StockData().drop_date()

        close_price = self.data['Close'].values

        close_price = close_price.reshape((-1))

        prediction_list = close_price[-self.look_back:]

        for i in range(num_prediction):

            x = prediction_list[-self.look_back:]
            x = x.reshape((1,self.look_back,1))

            #using the predict method from keras to generate the predicted values 

            out = self.model.predict(x)[0][0]

            prediction_list = np.append(prediction_list,out)


        prediction_list = prediction_list[self.look_back-1:]


        return prediction_list

    def get_pred_dates(self):

        split_percent =0.8
        num_prediction = 5

        self.data=self.data.reset_index(level=['Date'])

        date = self.data['Date']

        split = int(split_percent*len(date))

        date_train=date[:split]
        date_test=date[split:]

        last_date = date.values[-1]

        prediction_dates=pd.date_range(last_date,periods=num_prediction+1).tolist()


        return prediction_dates 
      

# stock_data=StockData()

# date=stock_data.get_pred_dates()

# print(date)
# print()
# #below will give the future prices and dates 


# list_prices=stock_data.predict_prices()
# print(list_prices)

