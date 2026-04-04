from datetime import date, datetime, timezone
from src.domain.virtual_objects.balance_vo import Balance
from src.domain.exceptions.exceptions import AgeRestrictionError
from src.domain.enums import Role
from typing import Optional

class User:    
    def __init__(self, user_id: Optional[int], name: str, surname: str, email: str,
                  birth_date: date, hashed_password: str, balance: int, role: str, created_at: datetime):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = email
        self.hashed_password = hashed_password
        self.balance = balance
        self.role = role
        self.birth_date = birth_date
        self.created_at = created_at

    def check_age(self):
        today = date.today()

        try:
            birthday_14 = self.birth_date.replace(year=self.birth_date.year + 14)
        except ValueError:
            # Для родившихся 29 февраля в високосный год
            birthday_14 = self.birth_date.replace(year=self.birth_date.year + 14, day=28)

        if birthday_14 > today:
            raise AgeRestrictionError("The user should be 14 or older")
    
    def check_age_GBA(self):
        today = date.today()

        try:
            birthday_18 = self.birth_date.replace(year=self.birth_date.year + 18)
        except ValueError:
            # Для родившихся 29 февраля в високосный год
            birthday_18 = self.birth_date.replace(year=self.birth_date.year + 18, day=28)

        if birthday_18 > today:
            raise AgeRestrictionError("The user should be 18 or older")
        
    def set_current_date(self):
        self.created_at = datetime.today()