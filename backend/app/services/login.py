from uuid import uuid4
from app.repository.login import LoginRepository
from app.db_config.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.requests.login import UserCreate


class LoginService: 
    
    def __init__(self,sess:Session = Depends(get_db)):
        self.repo = LoginRepository(sess)
        
    def get_login(self, username:str): 
        return self.repo.get_all_login_username(username)
    
    def create_user(self, user:UserCreate):         
        return self.repo.insert_login(user)