from src.domain.interfaces.unit_of_work import UnitOfWork
from src.application.DTO.admin_dto import CreateAdminDTO, ResponseAdminDTO 
from src.domain.entities.users.user_entity import User
from src.domain.virtual_objects.balance_vo import Balance
from datetime import datetime, timezone
from src.domain.exceptions.exceptions import UserAlreadyExistsError, DomainException
from src.domain.enums import Role

class RegisterAdminUC:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, dto: CreateAdminDTO, creator_role: str, hashed_password: str):
        async with self.uow:
            existing = await self.uow.users.get_by_email(dto.email)
            
            if existing:
                raise UserAlreadyExistsError("This user already exists")
            
            can_create = False
            if creator_role == Role.HEAD.value:
                if dto.role in [Role.VICE.value, Role.JUNIOR.value]:
                    can_create = True

            elif creator_role == Role.VICE.value:
                if dto.role == Role.JUNIOR.value:
                    can_create = True

            if not can_create:
                raise DomainException("You don't have permission to register user with this role")
            
            admin = User(
                user_id=None,
                name = dto.name,
                surname = dto.surname,
                email=dto.email,
                birth_date=dto.birth_date,
                hashed_password=hashed_password,
                balance=Balance(0).amount,
                created_at=datetime.now(timezone.utc),
                role=dto.role,
                is_admin=True
            )

            admin.check_age_admin()

            await self.uow.users.create(admin)
            await self.uow.commit()

            return self._to_response_dto(admin)
            
        
    @staticmethod
    def _to_response_dto(user: User):
        return ResponseAdminDTO(
            name = user.name,
            surname = user.surname,
            email=user.email
        )


