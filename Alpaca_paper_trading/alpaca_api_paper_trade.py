import alpaca_trade_api as tradeapi
import time
import logging
import threading
from datetime import datetime


def info_api_alpaca():

    
    key_id = 'YOUR KEY'
    secret_key = 'YOUR SECRET KEY'
    base_url = 'https://paper-api.alpaca.markets'


    api = tradeapi.REST(key_id, secret_key,base_url ,api_version='v2') # or use ENV Vars shown below
    account = api.get_account()
    print(account.status)

    return api
#TODO
#tests  to run check that the account is active 
#check the stocks choosen are avaialble to trade 
#check if market is open /weekends/weekdays 
#check api requests

api = info_api_alpaca()


#check if market is open
def check_market_open(api):

    clock = api.get_clock()
    if clock.is_open:
        print("the marrket is open")
        return True
    else:
        print("the market is closed")
        return False



#strategy for selling
def sell_strat(positions,api):


    for position in positions:
        # if position.symbol == assetsToTrade[stock]:

        #gives the you the percentage loss/gain
        x =float(position.unrealized_intraday_plpc)

        qty = int(position.qty)

        #can change different percentages
        #return positions to  sell full dict 

        if x >0.0 or  x<0.005:
            print("no change")
            return False
        elif x<-0.02 or x<-0.001:
            print(" selling loss")
            api.submit_order(str(position.symbol),qty,"sell","market","gtc") # Market order to fully close position
            print("selling",position.symbol)
            return True
        elif x>=0.01:
            print("start selling")
            api.submit_order(str(position.symbol),qty,"sell","market","gtc") # Market order to fully close position
            print("selling",position.symbol)
            return True
        else:
            pass 
            return False

#checking the prices
def check_prices(new_cash_bal,assetsToTrade,api):

    # can change time as desired 
    # "1H" # 1Min, 5Min, 15Min, 1H, 1D
    barTimeframe = "5min"

    open_list = []
    timeList = []
    openList = []
    highList = []
    lowList = []
    closeList = []
    volumeList = []

    if new_cash_bal>100:

        for asset in range(len(assetsToTrade)):

            symbol = assetsToTrade[asset]
            returned_data = api.get_barset(symbol,barTimeframe,limit=5)

            #time is EST  theorectically do not need to return as it is every hour
            time_in_nyc = returned_data[symbol][0].t
        
            openList.append(returned_data[symbol][0].o)
            highList.append(returned_data[symbol][0].h)
            closeList.append(returned_data[symbol][0].c)
            volumeList.append(returned_data[symbol][0].v)

                # lowList.append(returned_data[symbol][0].l)

    return openList,closeList



################################################################# strat1 ####################################################################

def buy_strat(assetsToTrade,openList,closeList,api):
    

    for stock in range(len(closeList)):
        # to  checks every price hour/timeframe

        bought_stock = []

        if closeList[stock]<openList[stock]:
            targetPositionSize = 10
            # 2 percent for test
            for asset in range(len(assetsToTrade)):
                stock_acq=api.submit_order(assetsToTrade[asset],targetPositionSize,"buy","market","gtc") # Market order to open position
                bought_stock.append(stock_acq)
                print("buying",asset)
            return True 
        else:
            pass
            return False 

def main():

    api = info_api_alpaca()
    #paper trading allows you to start of woth 100K
    api = info_api_alpaca()
    cashBalance = api.get_account().cash

    #I chose something smaller 60K
    new_cash_bal= float(cashBalance)*0.6
    print(new_cash_bal)
    assetsToTrade = ["AAPL","FB","WORK"]



    #only allow for 2 percent per stock can change
    positionSizing = 0.02
    positions = api.list_positions()

    #check open/close return boolean
    is_market_open = check_market_open(api)

    #need to thread as limit is 200 API requests 1hr chunks fixes the problem for now

    if is_market_open:

       openList,closeList =check_prices(cashBalance,assetsToTrade,api)

       x=sell_strat(positions,api)
        #need listss
       y=buy_strat(assetsToTrade,openList,closeList,api)

       while not x or not y:
          openList,closeList =check_prices(cashBalance,assetsToTrade,api)

          x =sell_strat(positions,api)
          y=buy_strat(assetsToTrade,openList,closeList,api)


    
    else:
        print("market is closed")