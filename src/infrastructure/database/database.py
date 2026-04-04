from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
from src.infrastructure.config import settings

#Здесь мы создаем фабрику сессии

SQL_ALCHEMY_DATABASE_URL = (settings.async_database_url)

engine = create_async_engine(
    SQL_ALCHEMY_DATABASE_URL,
    echo=True,
    future=True
)

async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
