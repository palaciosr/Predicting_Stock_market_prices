from sqlalchemy import Column, ForeignKey, Float, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# open high low close adj close volume    symbol
class StockData(Base):

    __tablename__ = 'stock_info'

    symbol = Column(String,primary_key =True)

    open = Column(Float,unique=True)
    close = Column(Float,unique=True)
    high = Column(Float,unique=True)
    low = Column(Float,unique=True)
    adj_close = Column(Float,unique=True)
    volume = Column(Integer,unique=True)




