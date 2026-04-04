from __future__ import annotations
from src.domain.exceptions.exceptions import InsufficientBalanceError

class Balance:
    def __init__(self, amount: int):
        if amount < 0:
            raise ValueError("the amount should not be negative")
        self.amount = amount
    
    def deposit(self, other: Balance):
        self.amount += other.amount

    def withdraw(self, other: Balance):
        new_amount = self.amount - other.amount
        if new_amount < 0:
            raise InsufficientBalanceError("Not enough money")
        self.amount = new_amount
    