from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.infrastructure.database.database import Base

class BookModel(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    book_name : Mapped[str] = mapped_column(nullable=False)
    publisher: Mapped[str] = mapped_column(nullable=False)
    isbn: Mapped[str] = mapped_column(nullable=False, unique=True)
    year: Mapped[int] = mapped_column(nullable=False)
    language: Mapped[str] = mapped_column(nullable=False)
    genre: Mapped[str] = mapped_column(nullable=False)
    pages: Mapped[int] = mapped_column(nullable=False)
    format: Mapped[str] = mapped_column(nullable=False)
    annotation: Mapped[str] = mapped_column(nullable=False)
    copies: Mapped["BookCopyModel"] = relationship(back_populates="book", cascade="all, delete-orphan")

class BookCopyModel(Base):
    __tablename__ = "book_copies"

    copy_id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.book_id"), nullable = False)
    copy_status: Mapped[str] = mapped_column(nullable=False)
    book: Mapped["BookModel"] = relationship(back_populates="copies")

