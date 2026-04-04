from src.domain.interfaces.unit_of_work import UnitOfWork

class DeleteBookUC:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, book_id: int):
        async with self.uow:
            result = self.uow.books.delete(book_id)
            await self.uow.commit()
            return result