import random
import pandas_datareader as web
import pandas as pd 

#predict for the next five days 
#week of June 8, 2020
#this comes from the last 6 months 
def last_six_months(min_price_6_months,max_price_6_months):

    six_month_price_data = []

    for sp500_price in range(4):

        six_month_price_data.append(random.randrange(int(min_price_6_months), int(max_price_6_months)))
    
    series_six_month_price_data = pd.Series(six_month_price_data)

    return series_six_month_price_data

def last_2wks(min_price_2wks,max_price_2wks):

    last_2wk_data = []

    for sp500_price in range(4):
       
        last_2wk_data.append(random.randrange(int(min_price_2wks), int(max_price_2wks)))

    series_last_2wk_data = pd.Series(last_2wk_data)

    return series_last_2wk_data

def actual_prices():

    data = web.DataReader('^GSPC',data_source='yahoo',start='2020-06-08',end='2020-06-12')

    data=data.reset_index(level=['Date'])

    return data['Date'],data['Open']

def all_pred():

    #we get a data with date and prices open close adjusted volume 
    data_6mo = web.DataReader('^GSPC',data_source='yahoo',start='2020-01-05',end='2020-06-05')

    min_price_6_months = data_6mo['Open'].min()
    max_price_6_months = data_6mo['Open'].max()

    #lets get random prices for the next 5 days given the last 6 months
    print("Prices given the last 6 months randomly")
    x=last_six_months(min_price_6_months,max_price_6_months)
    print()

    data_2wks = web.DataReader('^GSPC',data_source='yahoo',start='2020-05-03',end='2020-06-05')

    min_price_2wks = data_2wks['Open'].min()
    max_price_2wks = data_2wks['Open'].max()

    print("Prices given the last 2 weeks randomly")
    y=last_2wks(min_price_2wks,max_price_2wks)
    print()

    print("The actual prices for the prices for the week of June 8, 2020 ")
    z=actual_prices()

    return x,y,z 

x,y,z = all_pred()

print(x)
print(y)


    
