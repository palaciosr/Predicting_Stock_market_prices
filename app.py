from flask import Flask, request, render_template,redirect,session
import os, sys 
import pandas as pd 
import yfinance as yf
import plot 

from main import PredictionsAggregated

#visualizing
import simplejson as json
from bokeh.plotting import figure
from bokeh.palettes import Spectral11
from bokeh.embed import components 

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Stock_predictions.random_forest_prediction import MLPredictions

from Stock_predictions.ml_sp500 import StockData

app = Flask(__name__)

"""
the prediction gives a 98% score we should be wary of this 
It is important to note that this is a backtest as opposed to a forward test 
the only way to make money is to forward test I will conduct further research

"""

#used for getting a dataframe displayed
pred_prices = PredictionsAggregated().get_price_predictions()


@app.route('/')
def home():

    return render_template('home.html',tables=[pred_prices.to_html(classes='data')],titles=pred_prices.columns)


def stock_chosen_by_user(stock,start,end):

    data = yf.download(stock,data_source='yahoo',start=start,end=end)

    # df_prices_pred= StockData(data).predict_prices()

    return data 

def pred_prices(data):

    rf = MLPredictions(data)
    random_forest_prediction = rf.random_forest()

    return rf 

@app.route('/plot',methods=['GET','POST'])
def graph():


    if request.method == 'POST':

        stock = request.form['companyname']
        start = request.form['startdate']
        end = request.form['enddate']

        df = stock_chosen_by_user(stock,start,end)
        original_end = df['Close'][-1]

        rf = pred_prices(df)
        forecast_start = rf

        #wil return a series of the close
        random_forest_prediction = rf.random_forest()

    # stock_df =stock_df.reset_index(level=['Date'])

    # return render_template("plot.html",original = round(original_end,2),forecast=round(forecast_start,2),stock_tinker=stock.upper())

    return render_template("plot.html",stock_tinker=stock.upper())


if __name__ == '__main__':

    app.run()
