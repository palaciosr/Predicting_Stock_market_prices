from flask import Flask 
import os, sys 

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from Stock_averages.stock_averages import StockAverage

app = Flask(__name__)

@app.route('/')
def price():

    #sp 500 average and statistics 
    stock_avg,stock_stats= StockAverage().get_stock_average()

    print(type(stock_avg))

    return "the prices"


if __name__ == '__main__':

    app.run()