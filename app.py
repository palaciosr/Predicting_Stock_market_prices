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

app = Flask(__name__)

"""
the prediction gives a 98% score we should be wary of this 
It is important to note that this is a backtest as opposed to a forward test 
the only way to make money is to forward test I will conduct further research

"""

app.vars={}

pred_prices = PredictionsAggregated().get_price_predictions()


@app.route('/')
def home():

    return render_template('home.html',tables=[pred_prices.to_html(classes='data')],titles=pred_prices.columns)

#work in progress just gets price 
@app.route('/graph',methods=['GET','POST'])
def graph():

    app.vars['ticker'] = request.form['ticker']

    stock_df = yf.download(app.vars['ticker'], start='2020-06-17',end='2020-06-18')
    stock_df =stock_df.reset_index(level=['Date'])

    #attempt to not make an api call
    # app.vars['results'] = yf.download(app.vars['ticker'], start='2020-06-17',end='2020-06-18')
    # app.vars['results'] = app.vars['results'].reset_index(level=['Date'])

    p = figure(title='Stock prices displayed %s' % str(app.vars['ticker']),x_axis_label='date',x_axis_type='datetime')

    if request.form.get('Close'):
        
        p.line(x=stock_df['Date'].values,y=stock_df['Close'].values,line_width=2,legend_label="Close")
                
        # p.line(x=app.vars['results']['Date'].values,y=app.vars['results']['Close'].values,line_width=2,legend_label="Close")



    script, div = components(p)

    return render_template('graph.html',script=script,div=div)



if __name__ == '__main__':

    app.run()
