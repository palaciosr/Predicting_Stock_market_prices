from Stock_predictions.predition_random_prices import RandomGeneratePrices 
from Stock_predictions.ml_sp500 import StockData
import pandas as pd 

#multi-threading:
#https://towardsdatascience.com/multithreading-in-python-for-finance-fc1425664e74

"""
The following class gets prices in the following manner:
Dates in the future forward looking
Randomly generated prices for the previous 2 weeks
Randomly generated prices for the previous 2 months
Price prediction with time series generated via deep learning prices
Last the actual prices
"""

class ChooseStock:

    def get_stock(self):

        stock = input("Please input your favorite stock \n: ")
        stock =stock.upper()
        return stock


class PredictionsAggregated:

    def __init__(self):

        stock = ChooseStock().get_stock()

        self.stock_data = StockData(stock)
        self.deep_learning_prices = self.stock_data.predict_prices()

        self.random_last_6mo,self.random_last_2wks,self.date,self.actual_price = RandomGeneratePrices(stock).all_pred()


    def get_price_predictions(self):

        self.deep_learning_prices = pd.Series(self.deep_learning_prices)

        all_prices = pd.DataFrame({'Date':self.date,'Random_last_2wks':self.random_last_2wks,
                            'Random_last_6_months':self.random_last_6mo,'Deep_learning_prices_2months':self.deep_learning_prices,
                            'Actual_prices':self.actual_price})

        
        return all_prices

#code below is to check without the use of Flask  app.py
pred_prices = PredictionsAggregated().get_price_predictions()

print(pred_prices.head(4))