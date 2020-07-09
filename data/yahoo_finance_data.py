import sqlite3
import os 
from datetime import datetime
from app import db   

class Config:

    def create_db(self):

        #create the database for sp500 
        conn = sqlite3.connect('sp500.db')

    