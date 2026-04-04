from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError
from passlib.context import CryptContext

class PasswordHandler:
    def __init__(self):
        self.pwd_context = CryptContext(
            schemes=["argon2"],
            deprecated="auto"
        )

    def hash_password(self, plain_password: str):
        return self.pwd_context.hash(plain_password)
    
    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)
