from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get('/blog/{id}')
def show_post(id: int,limit:int=10,published:bool=True, sort:Optional[str]=None):
    if published:
        return{'data':f"user {id} has {limit} published blogs displayed"}
    else:
        return{'data':f"user {id} has {limit} blogs displayed"} 

@app.get("/about")
def about():
    return {'data':{
        'about_page'
    }}

class userBlog(BaseModel) :
    title:str
    body:str
    name:str
    age:int
    published:Optional[bool]
      
@app.post("/userblog") 
def post_blog(user:userBlog):
    return {f'user\'s blog title is: {user.title}'} 


#if __name__ == '__main__':
#  uvicorn.run(app,host="127.0.0.1",port=9000)
     