from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response

app = FastAPI()
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    
@app.get("/",status_code=200) 
def home():
    test = '{"name":"Johnss", "age":8, "car":null}'
    return Response(content=test, media_type="application/json")
