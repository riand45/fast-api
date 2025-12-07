from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import uuid
from src.config import Config
from fastapi import HTTPException
from itsdangerous import URLSafeTimedSerializer

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ACCESS_TOKEN_EXPIRE_MINUTES = 3600

def generate_password_hash(password: str) -> str:
    hash = password_context.hash(password)
    return hash

def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)

def create_access_token(user_data: dict, expiry: timedelta = None, refresh: bool = False):
    payload = {}

    payload["user"] = user_data
    payload["exp"] = datetime.utcnow() + (expiry or timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES))
    payload["jti"] = str(uuid.uuid4())
    payload["refresh"] = refresh

    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)

    return token

def decode_token(token: str):
    try:
        token_data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
        return token_data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

serializer = URLSafeTimedSerializer(secret_key=Config.JWT_SECRET_KEY, salt="email-configuration")

    