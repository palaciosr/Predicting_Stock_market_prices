import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import matplotlib 


#index that is consider the market sp500 check the risk
#we will try from Feb 2020 until where we see the COVID-19 effect 
sp500 = yf.download('^GSPC',data_source='yahoo',start='2020-02-01',end='2020-06-09')

#we want to get the log returns as this a metric that  'accurately' gives returns
sp500['log_returns'] = np.log(sp500['Close']/sp500['Close'].shift(1))
# print(sp500['log_returns'])

# assume we are interested in the log returns for a 20-day window  
sp500['Volatility'] = sp500['log_returns'].rolling(window=20).std()*np.sqrt(20)


print(sp500['Volatility'])

#we need a differnt IDE to see the plots 
# sp500[['Close', 'Volatility']].plot(subplots=True, color='blue',figsize=(8, 6)