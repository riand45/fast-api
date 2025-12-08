from fastapi import Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.errors import InvalidToken, AccessTokenRequired, RefreshTokenRequired
from .utils import decode_token
import time

class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        creds = await super().__call__(request)
        
        if creds is None:
            raise InvalidToken()
        
        token = creds.credentials

        token_data = decode_token(token)

        if not self.token_valid(token):
            raise InvalidToken()
        
        self.verify_token_data(token_data)

        return token_data

    def token_valid(self, token: str) -> bool:
        try:
            decode_token(token)
            return True
        except Exception:
            return False

    def verify_token_data(self, token_data: dict) -> bool:
        try:
            if not token_data["exp"] > time.time():
                raise InvalidToken()
            return True
        except Exception:
            return False


# Create functional dependencies that FastAPI can properly inject
token_bearer = HTTPBearer()

async def get_token_bearer(credentials: HTTPAuthorizationCredentials = Depends(token_bearer)) -> dict:
    """Dependency function to get and validate any token"""
    if credentials is None:
        raise InvalidToken()
    
    token = credentials.credentials
    token_data = decode_token(token)
    
    # Validate token
    try:
        decode_token(token)
    except Exception:
        raise InvalidToken()
    
    # Verify expiration
    try:
        if not token_data["exp"] > time.time():
            raise InvalidToken()
    except Exception:
        raise InvalidToken()
    
    return token_data


async def AccessTokenBearer(token_data: dict = Depends(get_token_bearer)) -> dict:
    """Dependency function to validate access tokens"""
    if token_data and token_data.get("refresh"):
        raise AccessTokenRequired()
    return token_data


async def RefreshTokenBearer(token_data: dict = Depends(get_token_bearer)) -> dict:
    """Dependency function to validate refresh tokens"""
    if token_data and not token_data.get("refresh"):
        raise RefreshTokenRequired()
    return token_data