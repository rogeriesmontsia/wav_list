
from jose import jwt, JWTError
from app.utils import config
from datetime import datetime, timedelta
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes 
from passlib.context import CryptContext

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

def create_access_token(data: dict, expires_after: timedelta):
    plain_text = data.copy()
    expire = datetime.utcnow() + expires_after
    plain_text.update({"exp": expire})
    encoded_jwt = jwt.encode(plain_text, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_password_hash(password):
    return crypt_context.hash(password)