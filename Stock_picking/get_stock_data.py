import pandas as pd 
import yfinance as yf 
import yahoofinancials
import datetime 

#input the stock ticker which will then download the data from yahoo finance 
print("please input the stock that you are interested in")
stock = input()


#we use yahoo finance to specify the dates 
stock_df = yf.download(stock, start='2020-01-01',end='2020-05-22')


#this will spit out a data frame with open,close,adj close, volume
print(stock_df.head())