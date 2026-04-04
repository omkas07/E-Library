class Book:
    def __init__(self, book_id: int, book_name: str, publisher: str, isbn: str, year: int,
                 lang: str, genre: str, pages: int, format: str, annotation: str):
        self.book_id = book_id
        self.book_name = book_name
        self.publisher = publisher
        self.isbn = isbn
        self.year = year
        self.lang = lang
        self.genre = genre
        self.pages = pages
        self.format = format
        self.annotation = annotation

    def add_copies(self, num: int):
        return num

    