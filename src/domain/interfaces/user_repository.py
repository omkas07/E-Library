from abc import ABC, abstractmethod
from src.domain.entities.users.user_entity import User

class IUserRepo(ABC):
    @abstractmethod
    async def create(self, user: User):
        pass

    @abstractmethod
    async def get_by_id(self, user_id: int):
        pass

    @abstractmethod
    async def get_by_email(self, email: str):
        pass

    @abstractmethod
    async def update(self, user: User):
        pass

    @abstractmethod
    async def delete(self, user: User):
        pass