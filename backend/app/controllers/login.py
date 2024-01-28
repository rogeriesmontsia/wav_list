from fastapi import APIRouter,Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.services.login import LoginService
from app.models.requests.login import LoginReq

router = APIRouter()

@router.post('/account',response_model=LoginReq)
def login_app(username:str, password:str, loginservice:LoginService = Depends(LoginService)):
    
    login = loginservice.get_login(username)
    return jsonable_encoder(login)
    