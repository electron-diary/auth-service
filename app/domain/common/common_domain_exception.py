from typing import Self


class CommonDomainException(Exception):
    def __init__(self: Self, message: str) -> None:
        super().__init__(message)