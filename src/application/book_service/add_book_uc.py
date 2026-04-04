from src.domain.interfaces.unit_of_work import UnitOfWork
from src.domain.entities.books.books_entity import Book
from src.application.DTO.book_dto import CreateBookDTO, ResponseBookDTO

class AddBookUc:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, dto: CreateBookDTO):
        async with self.uow:
            existing = await self.uow.books.get_by_isbn(dto.isbn)

            if existing:
                raise "csdfcsdcf"
            
            book = Book(
                book_name=dto.book_name,
                publisher=dto.publisher,
                isbn=dto.isbn,
                year=dto.year,
                lang=dto.lang,
                genre=dto.genre,
                pages=dto.pages,
                format=dto.format,
                annotation=dto.annotation
            )

            await self.uow.books.create(book)
            await self.uow.commit()


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