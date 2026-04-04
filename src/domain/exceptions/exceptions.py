class DomainException(Exception):
    def __init__(self, message: str, status_code: int = 400):
        super().__init__(message)
        self.status_code = status_code

class InsufficientBalanceError(DomainException):
    pass

class AgeRestrictionError(DomainException):
    def __init__(self, message: str):
        super().__init__(message, status_code = 403)

class UserAlreadyExistsError(DomainException):
    def __init__(self, message: str):
        super().__init__(message, status_code = 400)

class UnauthorizedError(DomainException):
    def __init__(self, message):
        super().__init__(message, status_code = 401)