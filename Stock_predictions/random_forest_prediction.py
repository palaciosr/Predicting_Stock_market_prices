import pandas as pd 
import numpy as np 
import sklearn 
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import yfinance as yf

"""
with this class I will back test the data with random forest 
which much like a decision tree,except a lot decison trees  put together
I will feed in the data from the Flask app 

"""

class MLPredictions:

    def __init__(self,data):


        self.data = data 

    #this method splits the data to  get 
    def data_split(self):
        
        X= self.data[['Open','High','Low','Volume']]
        y= self.data['Close']

        X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20)

        return X_train,X_test,y_train,y_test

    def random_forest(self):

        X_train,X_test,y_train,y_test = self.data_split()

        #instantiate random foresst with max features of 3 and 100 estimators 
        regression = RandomForestRegressor(max_depth=3,n_estimators=100)
        regression.fit(X_train,y_train)

        #grab the test data to make a prediction 
        prediction = regression.predict(X_test)

        #look at the score that we would get via 0.0-1.0 as regression problem
        #the closer we are to one the better the prediction 
        get_score= regression.score(X_test,y_test)

        return prediction 

        #would have to work with the max depth as there are not lots of features as of now 

#test case 
#consider case of having too little data 

"""
the prediction gives a 98% score we should be wary of this 
It is important to note that this is a backtest as opposed to a forward test 
the only way to make money is to forward test I will conduct further research
Uncomment below to test as a standalone module 
"""

#used for testing purposes


# print("input stock")
# stock = input()
# print()

# print("start input date yy=mm-dd")
# start = input()
# print()

# print("end input date yy=mm-dd")

# end = input()
# print()


# data = yf.download(stock,start=start,end=end)

# ml_pred= MLPredictions(data)

# x= ml_pred.random_forest()

# print(x)

