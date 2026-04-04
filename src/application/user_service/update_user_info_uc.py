from src.domain.interfaces.unit_of_work import UnitOfWork
from src.domain.entities.users.user_entity import User
from src.application.DTO.user_dto import UpdateUserDTO, ResponseUserDTO
from src.domain.exceptions.exceptions import UserNotFoundError

class UpdateUserInfo:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, user_id: int, dto: UpdateUserDTO):
        async with self.uow:
            user = await self.uow.users.get_by_id(user_id)
            if not user:
                raise UserNotFoundError("User was not found")
            
            if dto.name: user.name = dto.name
            if dto.surname: user.surname = dto.surname
            if dto.email: user.email = dto.email
            if dto.hashed_password: user.hashed_password = dto.hashed_password

            updated_user = await self.uow.users.update(user)
            await self.uow.commit()

            return self._to_response_dto(updated_user)
        
    @staticmethod
    def _to_response_dto(user: User):
        ResponseUserDTO(
            id = user.user_id,
            name = user.name,
            surname = user.surname 
        )