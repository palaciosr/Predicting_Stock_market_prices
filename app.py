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
# from Stock_picking import get_stock_data

app = Flask(__name__)

"""
the prediction gives a 98% score we should be wary of this 
It is important to note that this is a backtest as opposed to a forward test 
the only way to make money is to forward test I will conduct further research

"""

@app.route('/')
def main():
    return redirect('home.html')

#api key:

#pSwkUPQr8XpJf4xeFM7S


@app.route('/home.html',methods=['GET'])
def home():

    return render_template('home.html')


@app.route('/graph')
def graph():


    stock = input() = request.form()

    stock_df = yf.download(stock, start='2020-01-01',end='2020-05-22')

    stock_df =stock_df.reset_index(level=['Date'])


    p = figure(title='Stock prices displayed' % stock ,x_axis_label='date',x_axis_type='datetime')

    if request.form.get('Close'):
        
        p.line(x=stock_df['Date'].values,y=stock_df['Close'].values,line_width=2,legend="Close")


    script, div = components(p)

    return render_template('graph.html',script=script,div=div)






if __name__ == '__main__':

    app.run()



"""
#will come last but will  display multiple predictions

# @app.route('/')
# def prediction_power():

#     # ml_pred = MLPredictions()
#     # price_pred = ml_pred.random_forest()
#     x =last_six_months()

#     print("The prices predictions are ")

#     return render_template('home.html')
"""