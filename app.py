from flask import Flask 
import os, sys 

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


from Stock_predictions.random_forest_prediction import MLPredictions

from Stock_predictions.predition_random_prices import main 

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
    x,y,z =main()



    print("The prices are ")

    return x,y,z 


if __name__ == '__main__':

    app.run()