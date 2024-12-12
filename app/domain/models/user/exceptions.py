from typing import Self
from enum import Enum


class ErrorType(Enum):
    ...


class UserException(Exception):
    def __init__(
        self: Self, 
        error_type: ErrorType, 
        message: str
    ) -> None:
        super().__init__(message)

        self.error_type = error_type