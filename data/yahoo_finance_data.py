import sqlite3
import pandas as pd 
import yfinance as yf 

class StockData:

    def __init__(self):
        
        self.stock = '^GSPC'

    def get_stock_data(self):
        
        df_stock = yf.download(self.stock,period='5d',interval='30m')

        return df_stock