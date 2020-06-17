from flask import Flask, request, render_template,redirect,session
import os, sys 
import pandas as pd 
import yfinance as yf

#visualizing
import simplejson as json
from bokeh.plotting import figure
from bokeh.palettes import Spectral11
from bokeh.embed import components 

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


from Stock_predictions.random_forest_prediction import MLPredictions

from Stock_predictions.predition_random_prices import last_six_months 

app = Flask(__name__)

"""
the prediction gives a 98% score we should be wary of this 
It is important to note that this is a backtest as opposed to a forward test 
the only way to make money is to forward test I will conduct further research

"""

@app.route('/')
def prediction_power():

    # ml_pred = MLPredictions()
    # price_pred = ml_pred.random_forest()
    x =last_six_months()

    print("The prices predictions are ")

    return render_template('home.html')

@app.route('/graph')
def graph():



if __name__ == '__main__':

    app.run()