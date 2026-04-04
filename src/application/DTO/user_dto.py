from dataclasses import dataclass
from datetime import datetime

@dataclass
class CreateUserDTO:
    name: str
    surname: str
    email: str
    date: datetime

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
