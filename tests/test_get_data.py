import yfinance as yf 
import pandas as pd 
import os ,sys
from main import ChooseStock

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

stock = ChooseStock().get_stock()

# stock = yf.download("FB",data_source='yahoo',start='2020-07-01',end='2020-07-12')
# print(type(stock))

assert type(stock) == 'DataFrame'