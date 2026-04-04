from abc import ABC, abstractmethod
from src.domain.entities.books.books_entity import Book
from src.domain.entities.books.book_copy_entity import BookCopy

class IBookRepo(ABC):
    @abstractmethod
    async def create(self, book: Book):
        pass

    @abstractmethod
    async def get_by_id(self, book_id: int):
        pass

    @abstractmethod
    async def get_by_isbn(self, isbn: str):
        pass

    @abstractmethod
    async def update(self, book: Book):
        pass

    @abstractmethod
    async def delete(self, book_id: int):
        pass


class IBookCopyRepo(ABC):
    @abstractmethod
    async def create(self, book: BookCopy):
        pass

    @abstractmethod
    async def get_by_id(self, book_id: int):
        pass

    @abstractmethod
    async def get_by_isbn(self, isbn: str):
        pass

    @abstractmethod
    async def update(self, book: BookCopy):
        pass

    @abstractmethod
    async def delete(self, book_id: int):
        pass