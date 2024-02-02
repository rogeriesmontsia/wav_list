from dotenv import load_dotenv
import os

class ConfigLoader:
    def __init__(self, env_path=f"{os.getcwd()}/app/.env"):
        load_dotenv(env_path)
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.DATABASE = os.getenv("DATABASE")
        self.SECRET_KEY = os.getenv("SECRET_KEY")

