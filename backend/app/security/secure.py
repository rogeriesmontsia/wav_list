
from jose import jwt, JWTError
from app.utils import config
from datetime import datetime, timedelta
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes 
from passlib.context import CryptContext
from app.models.data.sqlalchemy_models import Users

SECRET_KEY = config.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
crypt_context = CryptContext(schemes=["sha256_crypt", "md5_crypt"])

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl='oauth2/authorize',
    tokenUrl="login/token",  
    scopes={ 
            "admin_read": "admin role that has read only role",
             "admin_write":"admin role that has write only role",
             "user":"valid user of the application",
             "guest":"visitor of the site" },
    )
def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)

def authenticate(username, password, account:Users):
    try:
        password_check = verify_password(password, account.password)
        return password_check
    except Exception as e:
        print(e)
        return False
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_password_hash(password):
    return crypt_context.hash(password)