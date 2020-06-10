import random
import pandas_datareader as web

#we get a data with date and prices open close adjusted volume 
data = web.DataReader('^GSPC',data_source='yahoo',start='2020-01-05',end='2020-06-05')

min_price = data['Open'].min()
max_price = data['Open'].max()

#predict for the next five days 
#week of June 8, 2020
for sp500_price in range(5):

    print(random.randrange(int(min_price), int(max_price))) 
