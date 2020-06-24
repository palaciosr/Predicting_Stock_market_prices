from Stock_predictions.predition_random_prices import all_pred 
from Stock_predictions.ml_sp500 import StockData
import pandas as pd 

#multi-threading:
#https://towardsdatascience.com/multithreading-in-python-for-finance-fc1425664e74



"""

"""
class PredictionsAggregated:

    def __init__(self):
        
        self.stock_data = StockData()
        # self.date = self.stock_data.get_pred_dates()
        self.deep_learning_prices = self.stock_data.predict_prices()
        self.random_last_6mo,self.random_last_2wks,self.date,self.actual_price = all_pred()


    def get_price_predictions(self):

        self.deep_learning_prices = pd.Series(self.deep_learning_prices)

        all_prices = pd.DataFrame({'Date':self.date,'Random_last_2wks':self.random_last_2wks,
                            'Random_last_6_months':self.random_last_6mo,'Deep_learning_prices_2months':self.deep_learning_prices,
                            'Actual_prices':self.actual_price})

        return all_prices

pred_prices = PredictionsAggregated().get_price_predictions()

print(pred_prices.head(4))