from .database import Base
from sqlalchemy import Column, Integer, String

class Product(Base):
    __tablename__= 'Product table'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    price=Column(String)
    number_of_stock_left=Column(String)
