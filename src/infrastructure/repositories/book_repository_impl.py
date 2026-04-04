from src.domain.interfaces.book_repository import IBookRepo, IBookCopyRepo
from src.domain.entities.books.books_entity import Book
from src.domain.entities.books.book_copy_entity import BookCopy
from src.infrastructure.database.models.book_model import BookModel, BookCopyModel
from src.domain.enums import BookCopyStatus

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

class IBookRepoImpl(IBookRepo):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, book: Book):
        db_book = BookModel(
            book_name = book.book_name,
            publisher = book.publisher,
            isbn = book.isbn,
            year = book.year,
            language = book.lang,
            genre = book.genre,
            pages = book.pages,
            format = book.format,
            annotation = book.annotation
        )

        self.session.add(db_book)
        await self.session.flush()

        return self._to_entity(db_book)

    async def get_by_id(self, book_id: int):
        result = await self.session.execute(select(BookModel).where(BookModel.book_id==book_id))

        db_book = result.scalar_one_or_none()
        return self._to_entity(db_book) if db_book else None
    
    async def get_by_isbn(self, isbn: str):
        result = await self.session.execute(select(BookModel).where(BookModel.isbn==isbn))

        db_book = result.scalar_one_or_none()
        return self._to_entity(db_book) if db_book else None
    
    async def update(self, book: Book):
        result = await self.session.execute(select(BookModel).where(BookModel.book_id==book.book_id))

        db_book = result.scalar_one()

        db_book.book_name = book.book_name
        db_book.publisher = book.publisher
        db_book.isbn = book.isbn
        db_book.year = book.year
        db_book.language = book.lang
        db_book.genre = book.genre
        db_book.pages = book.pages
        db_book.format = book.format
        db_book.annotation = book.annotation

        await self.session.flush()
        return self._to_entity(db_book)
    
    async def delete(self, book_id: int):
        result = await self.session.execute(select(BookModel).where(BookModel.book_id==book_id))

        db_book = result.scalar_one_or_none()

        if db_book:
            await self.session.delete(db_book)
            await self.session.flush()
            return True
        return False

    @staticmethod
    def _to_entity(db_book: BookModel):
        Book(
            book_name = db_book.book_name,
            publisher = db_book.publisher,
            isbn = db_book.isbn,
            year = db_book.year,
            lang = db_book.language,
            genre = db_book.genre,
            pages = db_book.pages,
            format = db_book.format,
            annotation = db_book.annotation
        )


class IBookCopyRepoImpl(IBookCopyRepo):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, copy: BookCopy):
        db_copy = BookCopyModel(
            book_id = copy.book,
            copy_status = copy.copy_status,
        )

        self.session.add(db_copy)
        await self.session.flush()

        return self._to_entity(db_copy)

    async def get_by_id(self, copy_id: int):
        result = await self.session.execute(select(BookCopyModel).where(BookCopyModel.copy_id==copy_id))

        db_copy = result.scalar_one_or_none()
        return self._to_entity(db_copy) if db_copy else None
    
    async def update(self, copy: BookCopy):
        result = await self.session.execute(select(BookCopyModel).where(BookCopyModel.copy_id==copy.copy_id))

        db_copy = result.scalar_one()

        db_copy.copy_status = copy.copy_status

        await self.session.flush()
        return self._to_entity(db_copy)
    
    async def delete(self, copy_id: int):
        result = await self.session.execute(select(BookCopyModel).where(BookCopyModel.copy_id==copy_id))

        db_copy = result.scalar_one_or_none()

        if db_copy:
            await self.session.delete(db_copy)
            await self.session.flush()
            return True
        return False

    @staticmethod
    def _to_entity(db_copy: BookCopyModel):
        BookCopy(
            book=db_copy.book,
            copy_status=db_copy.copy_status
        )