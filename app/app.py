from flask import Flask 

app = Flask(__name__)

@app.route('/')
def price():
    return "These are the prices"


if __name__ == '__main__':

    app.run()