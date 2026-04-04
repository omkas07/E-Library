from src.domain.interfaces.user_repository import IUserRepo
from src.domain.entities.users.user_entity import User
from src.infrastructure.database.models.user_model import UserModel

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class IUserRepoImpl(IUserRepo):

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User):
        db_user = UserModel(
            name = user.name,
            surname = user.surname,
            email = user.email,
            hashed_password = user.hashed_password,
            balance = user.balance,
            role = user.role,
            created_at = user.created_at,
            birth_date = user.birth_date
        )

        self.session.add(db_user)
        await self.session.flush()
        return self._to_entity(db_user)
    
    async def get_by_id(self, user_id: int):
        stmt = await self.session.execute(select(UserModel).where(UserModel.user_id == user_id))
        db_user = stmt.scalar_one_or_none()

        return self._to_entity(db_user) if db_user else None
    
    async def get_by_email(self, email: str):
        stmt = await self.session.execute(select(UserModel).where(UserModel.email==email))
        db_user = stmt.scalar_one_or_none()

        return self._to_entity(db_user) if db_user else None
    
    async def update(self, user: User):
        result = await self.session.execute(select(UserModel).where(UserModel.user_id==user.user_id))

        db_user = result.scalar_one()

        db_user.email = user.email
        db_user.name = user.name
        db_user.surname = user.surname
        db_user.hashed_password = user.hashed_password

        await self.session.flush()
        return self._to_entity(db_user)
    
    async def delete(self, user_id: int):
        result = await self.session.execute(select(UserModel).where(UserModel.user_id==user_id))

        db_user = result.scalar_one_or_none()

        if db_user:
            await self.session.delete(db_user)
            await self.session.flush()
            return True
        return False

    @staticmethod
    def _to_entity(db_user: UserModel):
        return User(
            user_id=db_user.user_id,
            name=db_user.name,
            surname=db_user.surname,
            email=db_user.email,
            hashed_password=db_user.hashed_password,
            balance=db_user.balance,
            birth_date=db_user.birth_date,
            role=db_user.role,
            created_at=db_user.created_at
        )

        