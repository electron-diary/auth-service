from typing import Self


class CommonDomainError(Exception):
    def __init__(self: Self, exception_message: str) -> None:
        self.message = exception_message
        super().__init__(self.message)


class DomainValidationError(CommonDomainError):
    ...
