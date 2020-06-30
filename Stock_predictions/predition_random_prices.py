import random
import pandas_datareader as web
import pandas as pd


#predict for the next five days 
#week of June 8, 2020
#this comes from the last 6 months 
class RandomGeneratePrices:

    def __init__(self,stock):
        
        # self.stock = ChooseStock().get_stock()

        self.actual_prices = web.DataReader(stock,data_source='yahoo',start='2020-06-08',end='2020-06-12')
    #we get a data with date and prices open close adjusted volume 
        self.data_6mo = web.DataReader(stock,data_source='yahoo',start='2020-01-05',end='2020-06-05')

        self.data_2wks = web.DataReader(stock,data_source='yahoo',start='2020-05-03',end='2020-06-05')

        self.stock = stock

        
    def last_six_months(self,min_price_6_months,max_price_6_months):

        six_month_price_data = []

        for sp500_price in range(5):

            six_month_price_data.append(random.randrange(int(min_price_6_months), int(max_price_6_months)))
        
        series_six_month_price_data = pd.Series(six_month_price_data)

        return series_six_month_price_data

    def last_2wks(self,min_price_2wks,max_price_2wks):

        last_2wk_data = []

        for sp500_price in range(5):
        
            last_2wk_data.append(random.randrange(int(min_price_2wks), int(max_price_2wks)))

        series_last_2wk_data = pd.Series(last_2wk_data)

        return series_last_2wk_data

    # def actual_prices(self):
        #'^GSPC'

        # data = web.DataReader(self.stock,data_source='yahoo',start='2020-06-08',end='2020-06-12')

        # self.actual_prices=self.actual_prices.reset_index(level=['Date'])

        # return self.actual_prices['Date'],self.actual_prices['Open']

    def all_pred(self):

    
        min_price_6_months = self.data_6mo['Open'].min()
        max_price_6_months = self.data_6mo['Open'].max()

        #lets get random prices for the next 5 days given the last 6 months
        # print("Prices given the last 6 months randomly")
        x=RandomGeneratePrices(self.stock).last_six_months(min_price_6_months,max_price_6_months)
        print()

        min_price_2wks = self.data_2wks['Open'].min()
        max_price_2wks = self.data_2wks['Open'].max()

        # print("Prices given the last 2 weeks randomly")
        y=RandomGeneratePrices(self.stock).last_2wks(min_price_2wks,max_price_2wks)
        print()

        # print("The actual prices for the prices for the week of June 8, 2020 ")
        # date,open_price=RandomGeneratePrices(self.stock).actual_prices()

        self.actual_prices=self.actual_prices.reset_index(level=['Date'])


        return x,y, self.actual_prices['Date'],self.actual_prices['Open']
        #date,open_price

# x,y,date,open_price=all_pred()
# print(x,y,date,open_price)



    
