from datetime import datetime, timedelta
from typing import Optional
from src.infrastructure.repositories.unit_of_work_impl import UnitOfWorkImpl
from src.infrastructure.security.jwt import JWTHandler
from src.infrastructure.security.password import PasswordHandler
from src.domain.entities.users.user_entity import User
from src.domain.exceptions.exceptions import UnauthorizedError

class AuthService():
    def __init__(self, uow: UnitOfWorkImpl, password_handler: PasswordHandler, jwt_handler: JWTHandler):
        self.uow = uow
        self.password_handler = password_handler
        self.jwt_handler = jwt_handler

    async def authenticate_user(self, email: str, password: str):
        async with self.uow:
            user = await self.uow.users.get_by_email(email)

            if not user:
                raise UnauthorizedError("Invalid credentials")
            
            if not self.password_handler.verify_password(password, user.hashed_password):
                raise UnauthorizedError("Invalid credentials")
            
            return user

    def create_access_token(self, user_id: int, expires_delta: Optional[timedelta] = None):
        return self.jwt_handler.create_access_token(
            data={"sub":str(user_id)},
            expires_delta=expires_delta
        )
    
    async def get_current_user(self, token: str):
        user_id = self.jwt_handler.decode_token(token)
        if not user_id:
            raise UnauthorizedError("Invalid token")
        
        async with self.uow:
            user = await self.uow.users.get_by_id(int(user_id))
            if not user:
                raise UnauthorizedError("user not found")
            
            return user