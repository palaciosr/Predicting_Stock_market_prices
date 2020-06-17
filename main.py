from Stock_predictions.predition_random_prices import all_pred 

from Stock_predictions.ml_sp500 import StockData

#multi-threading:
#https://towardsdatascience.com/multithreading-in-python-for-finance-fc1425664e74

stock_data= StockData()

date=stock_data.get_pred_dates()

print("dates and prices from the deep learning model")
print(date)
print()
#below will give the future prices and dates 


list_prices=stock_data.predict_prices()
print(list_prices)


all_pred()