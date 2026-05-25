from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

encode_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(user_input: str, hash: str) -> bool:
    return encode_context.verify(user_input, hash)

def hash_password(user_input: str) -> str:
    return encode_context.hash(user_input)

def create_access_token(data: dict, expire_time: Optional[timedelta] = None) -> str:
    origin = data.copy()
    if expire_time:
        expire = datetime.utcnow() + expire_time #refvisar
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.token_expire)

    origin.update({"exp": expire})
    jwt_Token = jwt.encode(origin, settings.auth_key, algorithm=settings.encode)

    return jwt_Token