import yfinance as yf 
import pandas as pd 
import os ,sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


from Stock_predictions.ml_sp500 import StockData


stock = yf.download("FB",data_source='yahoo',start='2020-07-01',end='2020-07-12')
# print(type(stock))

assert isinstance(stock,pd.DataFrame)



data = StockData.check_stock_exisits()

assert data == True