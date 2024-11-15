from typing import Self


class BaseDomainError(Exception):
    def __init__(self: Self, exception_message: str) -> None:
        self.message = exception_message
        super().__init__(self.message)
