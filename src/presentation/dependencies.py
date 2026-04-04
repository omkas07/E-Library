from src.infrastructure.database.database import async_session_maker
from src.infrastructure.repositories.unit_of_work_impl import UnitOfWorkImpl
from src.application.user_service import AuthService, RegisterUserUC
from src.infrastructure.security.password import PasswordHandler
from src.infrastructure.security.jwt import JWTHandler
from src.domain.exceptions.exceptions import UnauthorizedError

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")

def get_uow():
    return UnitOfWorkImpl(async_session_maker)

def get_password_handler():
    return PasswordHandler()

def get_user_register_uc(uow: UnitOfWorkImpl = Depends(get_uow)):
    return RegisterUserUC(uow)

def get_password_handler():
    return PasswordHandler()

def get_jwt_handler():
    return JWTHandler()

def get_auth_service(
    uow: UnitOfWorkImpl = Depends(get_uow),
    password_handler: PasswordHandler = Depends(get_password_handler),
    jwt_handler: JWTHandler = Depends(get_jwt_handler)
):
    return AuthService(uow, password_handler, jwt_handler)

async def get_current_user(
        token: str = Depends(oauth2_scheme),
        auth_service: AuthService = Depends(get_auth_service)
):
    try:
        user = await auth_service.get_current_user(token)
        return user
    except UnauthorizedError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate" : "Bearer"}
        )

