import sqlite3


def create_db():

    #create the database for sp500 
    conn = sqlite3.connect('sp500.db')

    