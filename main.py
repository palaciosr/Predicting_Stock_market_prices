from Stock_predictions.predition_random_prices import all_pred 

from Stock_predictions.ml_sp500 import StockData
import pandas as pd 

#multi-threading:
#https://towardsdatascience.com/multithreading-in-python-for-finance-fc1425664e74

stock_data= StockData()

date=stock_data.get_pred_dates()


deep_learning_prices=stock_data.predict_prices()
#numpy array
deep_learning_prices = pd.Series(deep_learning_prices)
# print(deep_learning_prices)

random_last_6mo,random_last_2wks,date,actual_price=all_pred()
  
all_prices = pd.DataFrame({'Date':date,'Random_last_2wks':random_last_2wks,
                            'Random_last_6_months':random_last_6mo,'Deep_learning_prices':deep_learning_prices,
                            'Actual_prices':actual_price})

print(all_prices.head(4))


# all_pred()

#create dataframe to show different scenarios 