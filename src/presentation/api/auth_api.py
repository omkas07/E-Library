from src.domain.exceptions.exceptions import DomainException, UnauthorizedError
from src.application.user_service.register_user_uc import RegisterUserUC
from src.application.DTO.user_dto import CreateUserDTO
from src.application.user_service.auth_user_uc import AuthService
from src.infrastructure.security.password import PasswordHandler
from src.infrastructure.config import settings
from src.presentation.schemas.user_schemas import UserCreate, UserResponse
from src.presentation.schemas.auth_schemas import TokenResponse, LoginRequest
from src.presentation.dependencies import get_password_handler, get_user_register_uc, get_auth_service

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from datetime import timedelta


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    user: UserCreate,
    password_handler: PasswordHandler = Depends(get_password_handler),
    usecase: RegisterUserUC = Depends(get_user_register_uc)
):
    try:
        hashed_password = password_handler.hash_password(user.password)
        dto = CreateUserDTO(
            name = user.name,
            surname = user.surname,
            email = user.email,
            birth_date = user.birt_date
        )
        user = await usecase.execute(dto, hashed_password)
        return user
    except DomainException as e: 
        raise HTTPException(status_code=e.status_code, detail=str(e))
    
@router.post("/login", response_model=TokenResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    try:
        user = await auth_service.authenticate_user(form_data.username, form_data.password)
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = auth_service.create_access_token(user.user_id, access_token_expires)
        return TokenResponse(access_token=access_token)
    except UnauthorizedError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers= {"WWW-Authenticate":"Bearer"}
        )
