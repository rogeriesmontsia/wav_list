from typing import Union
from fastapi import FastAPI
from app.db_config.database import Base
from app.db_config.database import engine
from app.controllers import login

Base.metadata.create_all(bind=engine) 
app = FastAPI()

def configure():
    app.include_router(login.router, prefix="/login")
    
configure()


@app.get("/products")
def read_root():
    '''TODO petició api X'''
    return {"producte1": "asdfasdfsadfdsaf"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "qss": q}


    