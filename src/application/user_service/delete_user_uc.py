from src.domain.interfaces.unit_of_work import UnitOfWork
from src.domain.entities.users.user_entity import User

class DeleteUserUC:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, user_id: int):
        async with self.uow:
            result = await self.uow.users.delete(user_id)
            await self.uow.commit()
            return result