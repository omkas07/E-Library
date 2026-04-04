from src.domain.enums import BookCopyStatus

class BookCopy:
    def __init__(self, book_copy_id: int, book: int, copy_status: BookCopyStatus):
        self.book_copy_id = book_copy_id
        self.book = book
        self.copy_status = copy_status


