from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Load .env file
path ="{}/app/.env".format(os.getcwd())
load_dotenv(path)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DATABASE")
DB_URL = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DATABASE)
engine = create_engine(DB_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()