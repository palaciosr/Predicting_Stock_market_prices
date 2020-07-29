import yfinance as yf 
import pandas as pd 
import os ,sys


stock = yf.download("FB",data_source='yahoo',start='2020-07-01',end='2020-07-12')
# print(type(stock))

assert isinstance(stock,pd.DataFrame)