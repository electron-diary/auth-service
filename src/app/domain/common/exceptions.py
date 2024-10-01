from typing import Self

class DomainException(Exception):
    def __init__(self: Self, message: str) -> None:
        self.message = message

class DomainValidationError(DomainException):
    pass

class AuthentificationError(DomainException):
    pass

