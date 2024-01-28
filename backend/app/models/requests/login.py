from pydantic import BaseModel


class LoginReq(BaseModel): 
    username: str 
    password: str
    
class UserCreate(BaseModel): 
    username: str 
    password: str
    email: str