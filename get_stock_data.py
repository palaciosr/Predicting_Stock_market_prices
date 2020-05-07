import pandas as pd 
import yfinance as yf 
import yahoofinancials
import datetime 

print("please input the stock that you are interested in")
stock = input()


time_min="5m"
days="1d"

stock_df = yf.download(stock, interval=time_min,period=days)

print(stock_df.head())