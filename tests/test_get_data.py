import yfinance as yf 
import pandas as pd 
import os ,sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


stock = yf.download("FB",data_source='yahoo',start='2020-07-01',end='2020-07-12')

assert isinstance(stock,pd.DataFrame)



#test for flask 
#https://www.patricksoftwareblog.com/unit-testing-a-flask-application/