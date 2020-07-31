# Research_and_design_with_deep_learning_and_Stock_price_movements

This project is an attempt to predict the U.S. S&P 500 index. Simply it is a POC on the performance of long term short term memory deep learning algorithimns. I use the historical prices of the S&P 500 index, and see the performance. Note this for now May 3, 2020 is only using prices and volume. There are more features to add along with a frontend as well.

# Assumptions 
I will not be creating an API to consume rather I will consume yahoo finance API consume to get the following: Open, High, Low, Adj. Close, Volume. Similarly, for deep learning techniques I will be using exisiting frameworks, as those open source produce good enough results for the testing purposes I need.

# Running this module 
There are  two ways to run this module, clone it.Once that is done,then, assuming you have python 3.0 and pip installed.
``` do bash run.sh. ```
Otherwise, do a pip install -r requirements.txt then, run python main.py this will open up the terminal. You can also after installing the dependencies, run python app.py to display to your local host. Note this section requires input before it outputs anything you would have to choose a stock of your choosing such as MSFT as it stands you have to input the stock ticker twice (will be enabled and disabled with development, but ideally will only need to be inputted once in the future).

# Explanation of the output
The output will give you a dataframe (essentially like any SQL relational DB would or csv headers with rows). The columns are: Date, Random_last_2wks, Random_last_6_months,Deep_learning_prices_2months, and actual prices. All of the dates are currently set, however, these were forward looking dates such that we generate future prices as opposed to backtesting. The columns labelled 'Random' are generated via Python's random number generator, whereby I take the date for the given time frame and get the min and max prices, after, I generate the random prices. The randomly generated prices are very inaccurate as when compare them to the actual prices they are off by hundreds of dollars. Most important column for prediction is the LSTM (Keras package) generated prices, we use deep learning technique called LSTM explained below. As we can prove for ourselves, this does a much better job than randomly generated prices. The main reason for this is that we are to a large extent doing a f(x) = y_1+y_n +e, where y represents features (columns) and e represents error. In any forecasting, we try to curve fit the data, such that it produces a curve that is not definitve such as linear or expontential, but rather numeric. Additionally, as the name implies long-term short-term memory, the neural network forgets the extreme past and focus only on the short-term past. Therefore, arriving at better results than just pure randomness. 

# Long Term short term memory (LSTM)

This project is to examine what LSTMs can do to predict stock market data. As the term implies, there this deep learning method is designed to be able to model both long term and short term events. Deep learning LSTM seems to be the best candidate as of now 
compared to randomly generating prices. However, it still not accurate when we look at the actual prices.


# Research 

There are various articles, to which I will refer to later ,where they state that this deep learning model does not work. This is an exercise where I attempt to validate the results of others, as well as build a price generator with Keras.

One way to measure what deep learning offers of value add is to simply see the statistics for the given stock(s) or index. I have included the folder "Stock_averages" as both a metric and for seeing if a holding strategy is better or buying and selling. 

Indeed, if we could time the market buy and hold won't be as effective, until there is enough relevant data for machine learnign models, then I can say with confidence at minumum, I can match the return on investment (ROI), of the SP500

# Alpaca Trading module
Alpaca trading allows you to paper trade and/or live trade. The one way to test your models ML or otherwise, is to backtest. However, most of the time backtest will fail in the future as the trading world is dynammic. Create an API key and follow the documentation: https://alpaca.markets/docs/. The streamer is currently a work in progress, with hope that anyone can choose anytime frame and have it streaming locally or on the cloud (once profitable). The alpaca paper trading module uses a simple strategy (which should not be used unless you know what you are doing), it is used here for testing purposes. Although, not perfect it satisfies are requirement of both funnctionality and (luckily) profitability. Most importantly, this module can be ran automatically, which I will further develop. Note that there needs to be rigorous testing for strategies, as this can be made into a real account by changing the endpoint,  approach with caution. To run this module make sure you have the alpaca installed pip install alpaca-trade-api. Then run python alpaca_paper_trade_api.py when the market is open 9:30 AM-1:00 PM EST.
