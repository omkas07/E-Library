from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class CreateUserDTO:
    name: str
    surname: str
    email: str
    birth_date: date

@dataclass
class ResponseUserDTO:
    name: str
    surname: str
    email: str

@dataclass
class UpdateUserDTO:
    name: str
    surname: str
    email: str
    hashed_password: str
