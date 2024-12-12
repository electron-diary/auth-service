from typing import Self
from enum import Enum


class ErrorType(Enum):
    USER_INACTIVE = "user_inactive"
    INVALID_CONTACTS = 'invalid_contacts'
    INVALID_FULLNAME = 'invalid_fullname'
    PROFILE_INACTIVE = 'profile_inactive'
    NOT_FOUND = 'not_found'


class UserException(Exception):
    def __init__(
        self: Self, 
        error_type: ErrorType, 
        message: str
    ) -> None:
        super().__init__(message)

        self.error_type = error_type