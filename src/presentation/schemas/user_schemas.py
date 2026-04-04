from pydantic import BaseModel, EmailStr
from datetime import datetime, date

class UserCreate(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    birt_date: date

class UserResponse(BaseModel):
    name: str
    surname: str
    email: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"