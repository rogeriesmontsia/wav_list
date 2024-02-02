from typing import Union
from fastapi import FastAPI
from app.db_config.database import Base
from app.db_config.database import engine
from app.controllers.config_loader import ConfigLoader
# from app.controllers import login
from dotenv import load_dotenv
import os

app = FastAPI()

# def configure():
#     app.include_router(login.router, prefix="/login")
    
# configure()

# Base.metadata.create_all(bind=engine) 

@app.get("/products")
def read_root():
    return {"producte1": "asdfasdfsadfdsaf"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "qss": q}

config_loader = ConfigLoader()
@app.get("/env-user")
def env_user():
    return config_loader.DB_USER

print(config_loader.DB_USER)
print(config_loader.DB_PASSWORD)
print(config_loader.DB_HOST)
print(config_loader.DB_PORT)
print(config_loader.DATABASE)
print(config_loader.SECRET_KEY)