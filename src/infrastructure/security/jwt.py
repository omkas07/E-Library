from jose import JWTError, jwt
from typing import Optional
from datetime import datetime, timedelta
from src.infrastructure.config import settings

class JWTHandler:
    def __init__(self):
        self.secret_key = settings.JWT_SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.access_token_expire_on_minute = settings.ACCESS_TOKEN_EXPIRE_MINUTES

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now()+expires_delta
        else:
            expire = datetime.now()+timedelta(minutes=self.access_token_expire_on_minute)

        to_encode.update({"exp":expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def decode_token(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            user_id: str = payload.get("sub")
            if user_id is None:
                return None
            return user_id
        except JWTError:
            return None