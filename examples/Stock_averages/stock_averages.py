import math 
import pandas as pd 
import pandas_datareader as web


class StockAverage:

    def __init__(self):
        
        self.data = web.DataReader('^GSPC',data_source='yahoo',start='2020-01-01',end='2020-06-01')

    
    def get_stock_average(self):


        sp_500_mean = self.data['Open'].mean()
        sp_stats = self.data['Open'].describe()

        return sp_500_mean,sp_stats


stock_average_class= StockAverage()

avg_price, stats_sp_500 = stock_average_class.get_stock_average()

print(type(avg_price))

# print("SP500 average price for the last 6 months")
# print(avg_price)



# print()
# print("Stats on the SP500")
# print(stats_sp_500)
