from typing import Union
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
def read_root():
    '''TODO petició api X'''
    return {"producte1": "asdfasdfsadfdsaf"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "qss": q}

if __name__ == '__main__':
    uvicorn.run("main:app",host="127.0.0.1",port=8181,reload=True)