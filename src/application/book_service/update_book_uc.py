from src.domain.interfaces.unit_of_work import UnitOfWork
from src.application.DTO.book_dto import UpdateBookDTO, ResponseBookDTO
from src.domain.entities.books.books_entity import Book

class UpdateBookUC:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, book_id: int, dto: UpdateBookDTO):
        async with self.uow:
            book = await self.uow.books.get_by_id(book_id)

            if not book:
                raise "dfvd"
            
            if dto.book_name: book.book_name = dto.book_name
            if dto.publisher: book.publisher = dto.publisher
            if dto.isbn: book.isbn = dto.isbn
            if dto.year: book.year = dto.year
            if dto.lang: book.lang = dto.lang
            if dto.genre: book.genre = dto.genre
            if dto.pages: book.pages = dto.pages
            if dto.format: book.format = dto.format
            if dto.annotation: book.annotation = dto.annotation
            
            updated_book = await self.uow.books.update(book)
            await self.uow.commit()
            return self._to_response_dto(updated_book)

    @staticmethod
    def _to_response_dto(book: Book):
        return ResponseBookDTO(
                book_name=book.book_name,
                publisher=book.publisher,
                isbn=book.isbn,
                year=book.year,
                lang=book.lang,
                genre=book.genre,
                pages=book.pages,
                format=book.format,
                annotation=book.annotation
        )