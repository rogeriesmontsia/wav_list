from fastapi import APIRouter,Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.services.login import LoginService
from app.models.requests.login import LoginReq,UserCreate
import re
router = APIRouter()

pattern_email =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

@router.post('/account',response_model=LoginReq)
def login_app(user:LoginReq, loginservice:LoginService = Depends(LoginService)):
    
    login = loginservice.get_login(user.username)
    if login is None:
        return JSONResponse(status_code=404, content="User not found")
    return jsonable_encoder(login)

@router.post('/register')
def login_app(user:UserCreate, loginservice:LoginService = Depends(LoginService)):    
    if re.match(pattern_email, user.email):
        login = loginservice.create_user(user)
        if not login:
            return JSONResponse(status_code=500, content="User not created")
    else:
        return JSONResponse(status_code=500, content="Email not valid")
    return jsonable_encoder(login)
    