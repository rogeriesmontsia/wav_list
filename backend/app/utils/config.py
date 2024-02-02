from dotenv import load_dotenv
import os

# Load .env file
path ="{}/app/.env".format(os.getcwd())
load_dotenv(path)

#database configuration
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DATABASE = os.getenv("DATABASE")
DB_URL = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DATABASE)