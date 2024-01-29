from typing import Union
from fastapi import FastAPI
from app.db_config.database import Base
from app.db_config.database import engine
from app.controllers import login


app = FastAPI()

def configure():
    app.include_router(login.router, prefix="/login")
    
configure()



@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine) 

@app.get("/products")
def read_root():
    return {"producte1": "asdfasdfsadfdsaf"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "qss": q}


    