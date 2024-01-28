
from typing import Dict, Any
from sqlalchemy.orm import Session
from app.models.data.sqlalchemy_models import Users
from sqlalchemy import desc
from fastapi.params import Depends
from app.db_config.database import get_db

class LoginRepository: 
    def __init__(self, sess:Depends(get_db)):
        self.sess:Session = sess
    
    def insert_login(self, login: Users) -> bool: 
        try:
            self.sess.add(login)
            self.sess.commit()
        except Exception as e:
            print(e) 
            return False 
        return True
    
    def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
       try:
             self.sess.query(Users).filter(Users.id == id).update(details)     
             self.sess.commit() 
           
       except: 
           return False 
       return True
   
    def delete_login(self, id:int) -> bool: 
        try:
           login = self.sess.query(Users).filter(Users.id == id).delete()
           self.sess.commit()
        except: 
            return False 
        return True
    
    def get_all_login(self):
        return self.sess.query(Users).all() 
    
    def get_all_login_username(self, username:str):
        #print(self.str)
        return self.sess.query(Users).filter(Users.username == username).one_or_none()
    
    def get_all_login_sorted_desc(self):
        return self.sess.query(Users.username, Users.password).order_by(desc(Users.username)).all() 
    
    def get_login(self, id:int): 
        return self.sess.query(Users).filter(Users.id == id).one_or_none()
