from src.domain.interfaces.unit_of_work import UnitOfWork
from src.application.DTO.user_dto import CreateUserDTO, ResponseUserDTO
from src.domain.entities.users.user_entity import User
from src.domain.virtual_objects.balance_vo import Balance
from datetime import datetime, timezone
from src.domain.exceptions.exceptions import UserAlreadyExistsError
from src.domain.enums import Role
from src.infrastructure.config import settings

class RegisterUserUC:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, dto: CreateUserDTO, hashed_password: str):
        async with self.uow:
            existing = await self.uow.users.get_by_email(dto.email)
            
            if existing:
                raise UserAlreadyExistsError("Already have this user with this email")
            
            flag = False

            if dto.email == settings.INITIAL_ADMIN_EMAIL:
                admin = Role.HEAD.value
                flag = True
            else: admin = Role.USER.value
            
            user = User(
                user_id=None,
                name = dto.name,
                surname = dto.surname,
                email=dto.email,
                birth_date=dto.birth_date,
                hashed_password=hashed_password,
                balance=Balance(0).amount,
                created_at=datetime.now(timezone.utc),
                role=admin,
                is_admin=flag
            )

            user.check_age()


            await self.uow.users.create(user)
            await self.uow.commit()

            return self._to_response_dto(user)

    @staticmethod
    def _to_response_dto(user: User):
        return ResponseUserDTO(
            name = user.name,
            surname = user.surname,
            email=user.email
        )