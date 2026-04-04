from sqlalchemy.orm import Mapped, mapped_column
from src.infrastructure.database.database import Base
from sqlalchemy import TIMESTAMP, DateTime, text, String, Text
from datetime import datetime, date

class UserModel(Base):
    __tablename__='users'
    user_id : Mapped[int] = mapped_column(primary_key=True, nullable = False)
    name : Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(Text, nullable=False)
    role: Mapped[str] = mapped_column(nullable=False)
    balance: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    birth_date: Mapped[date] = mapped_column(nullable=False)
