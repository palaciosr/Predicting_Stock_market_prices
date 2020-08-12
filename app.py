from flask import Flask, request, render_template,redirect,session
import os, sys 
import pandas as pd 
import yfinance as yf
import plot 


#visualizing
import simplejson as json
from bokeh.plotting import figure
from bokeh.palettes import Spectral11
from bokeh.embed import components 

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Stock_predictions.random_forest_prediction import MLPredictions

# from Stock_predictions.ml_sp500 import StockData

# from main import PredictionsAggregated

app = Flask(__name__)

"""
the prediction gives a 98% score we should be wary of this 
It is important to note that this is a backtest as opposed to a forward test 
the only way to make money is to forward test I will conduct further research

"""


def forward_pred():
    #used for getting a dataframe displayed
    pred_prices = PredictionsAggregated().get_price_predictions()
    # print(pred_prices.head(5))

    return pred_prices

@app.route('/forward_predictions')
def forward_predictions():

    pred_prices = forward_pred()

    return render_template('forward_predictions.html',tables=[pred_prices.to_html(classes='data')],titles=pred_prices.columns)

@app.route('/')
def home():

    return render_template("index.html")

def stock_chosen_by_user(stock,start,end):

    data = yf.download(stock,data_source='yahoo',start=start,end=end)

    return data 

def pred_prices(data):

    rf = MLPredictions(data)
    random_forest_prediction = rf.random_forest()

    return rf 

@app.route('/plot',methods=['GET','POST'])
def main():

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

    # return render_template("plot.html",original = round(original_end,2),forecast=round(forecast_start,2),stock_tinker=stock.upper())

    return render_template("plot.html",original = original_end,forecast=random_forest_prediction[-1],stock_tinker=stock.upper())




if __name__ == '__main__':

    app.run()
