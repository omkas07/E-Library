from pydantic import BaseModel, EmailStr
from datetime import datetime, date

class AdminCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    role: str
    birt_date: date

class AdminResponse(BaseModel):
    name: str
    surname: str
    email: str
