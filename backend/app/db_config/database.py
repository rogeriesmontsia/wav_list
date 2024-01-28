from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DB_USER = "user"
DB_PASSWORD = "password"
DB_HOST = "database"
DB_PORT = 3306
DATABASE = "mydatabase"
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