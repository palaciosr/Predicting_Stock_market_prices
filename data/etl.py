import sqlalchemy
from sqlalchemy import Column, ForeignKey, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import sys
from os import listdir 
from sqlalchemy.orm import sessionmaker

from yahoo_finance_data import StockData

Base = declarative_base()

# columns open high low close adj close volume    symbol
class StockData(Base):

    __tablename__ = 'stock_info'

    symbol = Column(String,primary_key =True)

    open = Column(Float,unique=True)
    close = Column(Float,unique=True)
    high = Column(Float,unique=True)
    low = Column(Float,unique=True)
    adj_close = Column(Float,unique=True)
    volume = Column(Integer,unique=True)


# seperation of db initiation
file_name = 'new_stock_data/' + listdir('new_stock_data')[0]

#holds stock df 
new_data = StockData().get_stock_data()


database_location = "sqlite:///stock_db.sqlite"
engine = sqlalchemy.create_engine(database_location)

Session = sessionmaker(bind = engine)
session = Session()

for stock_info in new_data.to_dict(orient='records'):
    
    stock_data = StockData(
        open = stock_info['Open'],
        close = stock_info['Close'],
        high = stock_info['High'],
        low = stock_info['Low'],
        adj_close = stock_info['Adj. Close'],
        volume = stock_info['Volume'])

    session.add(stock_data)
    
session.commit()