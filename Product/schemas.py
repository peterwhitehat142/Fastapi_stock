from pydantic import BaseModel

class user_Product(BaseModel):
    name:str
    price:float
    number_of_stock_left:int