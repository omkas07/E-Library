from dataclasses import dataclass
from datetime import date

@dataclass
class CreateAdminDTO:
    name: str
    surname: str
    email: str
    role: str
    birth_date: date

@dataclass
class ResponseAdminDTO:
    name: str
    surname: str
    email: str