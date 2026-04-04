from dataclasses import dataclass

@dataclass
class CreateBookDTO:
    book_name: str 
    publisher: str
    isbn: str
    year: int    
    lang: str
    genre: str
    pages: int
    format: str
    annotation: str

@dataclass
class ResponseBookDTO:
    book_name: str
    publisher: str
    isbn: str
    year: int    
    lang: str
    genre: str
    pages: int
    format: str
    annotation: str

@dataclass
class UpdateBookDTO:
    book_name: str
    publisher: str
    isbn: str
    year: int    
    lang: str
    genre: str
    pages: int
    format: str
    annotation: str

@dataclass
class UpdateBookCopyDTO:
    status: str