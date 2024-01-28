from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, Text
from sqlalchemy.orm import relationship
from app.db_config.database import Base


class Users(Base): 
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=False, index=False)
    password = Column(String(100), unique=False, index=False)