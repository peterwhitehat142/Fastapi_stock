from fastapi import FastAPI, Depends, status,HTTPException
from pydantic import BaseModel
from .schemas import user_Product
from .database import Base,engine, local_session
from .models import Product
from sqlalchemy.orm import Session



Productapp=FastAPI()

Base.metadata.create_all(engine)

@Productapp.get('/')
def root():
    return {"Welcome to GB brand"}

def get_db():
    db=local_session()
    try:
        yield db
    finally:
        db.close()    

@Productapp.post("/product_upload",status_code=status.HTTP_201_CREATED)
def create(user:user_Product,db:Session=Depends(get_db)):
    new_product= Product(name=user.name, price=user.price,number_of_stock_left=user.number_of_stock_left)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return f"The product uploaded is {new_product}"

@Productapp.delete('/product{id}')
def destroy(id,db:Session=Depends(get_db),status_code=status.HTTP_204_NO_CONTENT):
    db.query(Product).filter(Product.id==id).delete(synchronize_session=False)
    db.commit()
    return f"User with id {id} is deleted"

@Productapp.put("/product{id}")
def update(id,user:user_Product,db:Session=Depends(get_db),status_code=status.HTTP_202_ACCEPTED):
    product_obj=db.query(Product).filter(Product.id==id)
    if not product_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'product with id {id} do not exists')
    product_obj.update(user)
    db.commit()
    return 'Updated'

@Productapp.get("/allproductlist")
def all(db:Session=Depends(get_db)):
    products= db.query(Product).all()
    return products



@Productapp.get("/product{id}",status_code=status.HTTP_201_CREATED)
def show(id,db:Session=Depends(get_db)):
    id_data=db.query(Product).filter(Product.id==id).first()
    if not id_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Product with id {id} not found')
    return id_data