from src.domain.exceptions.exceptions import DomainException
from src.domain.entities.users.user_entity import User
from src.application.admin_service.register_admin_uc import RegisterAdminUC
from src.application.DTO.admin_dto import CreateAdminDTO
from src.infrastructure.security.password import PasswordHandler
from src.presentation.schemas.admin_schemas import AdminCreate, AdminResponse
from src.presentation.dependencies import get_password_handler, get_admin_register_uc, get_current_user

from fastapi import APIRouter, HTTPException, status, Depends


router = APIRouter(prefix="/admin/auth", tags=["Admins Authentication"])

@router.post("/register", response_model=AdminResponse, status_code=status.HTTP_201_CREATED)
async def register(
    admin: AdminCreate,
    password_handler: PasswordHandler = Depends(get_password_handler),
    usecase: RegisterAdminUC = Depends(get_admin_register_uc),
    current_user: User = Depends(get_current_user)
):
    if not current_user.is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied")
    try:
        hashed_password = password_handler.hash_password(admin.password)
        dto = CreateAdminDTO(
            name = admin.name,
            surname = admin.surname,
            email = admin.email,
            role = admin.role,
            birth_date = admin.birt_date
        )
        reg_admin = await usecase.execute(dto, current_user.role, hashed_password)
        return reg_admin
    except DomainException as e: 
        raise HTTPException(status_code=e.status_code, detail=str(e))