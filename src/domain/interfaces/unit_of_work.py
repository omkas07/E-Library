from abc import ABC, abstractmethod
from src.domain.interfaces.user_repository import IUserRepo
from src.domain.interfaces.book_repository import IBookRepo, IBookCopyRepo

#Здесь интерфейс для UoW

class UnitOfWork(ABC):
    users: IUserRepo
    books: IBookRepo
    copy: IBookCopyRepo

    @abstractmethod
    async def __aenter__(self):
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc, tb):
        pass

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass