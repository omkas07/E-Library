from src.domain.interfaces.unit_of_work import UnitOfWork

class LoginUserUc:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

