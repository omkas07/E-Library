from src.domain.interfaces.unit_of_work import UnitOfWork
from src.infrastructure.repositories.user_repository_impl import IUserRepoImpl
from src.infrastructure.repositories.book_repository_impl import IBookRepoImpl
from sqlalchemy.ext.asyncio import AsyncSession

class UnitOfWorkImpl(UnitOfWork):
    def __init__(self, session_factory):
        self.session_factory = session_factory #Сюда мы кладем фабрику сессии

    async def __aenter__(self):
        self.session: AsyncSession = self.session_factory() #Здесь присваевываем сессеию как атрибут
        self.users = IUserRepoImpl(self.session) #Здесь тоже аттрибут
        self.books = IBookRepoImpl(self.session)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        try:
            if exc_type is not None:
                await self.rollback()
        finally:
            await self.session.close()

    async def commit(self):
        await self.session.commit()
    
    async def rollback(self):
        await self.session.rollback()


"""
Мы используем UoW что бы гарантировать атомарность транзакции.
То есть не использовать commit дважды.
Например если у user и wallet будут каммиты, то один из них могут не сработать а это нарушает 
атомарность.
С помощью UoW коммиты происходят за один раз.
"""