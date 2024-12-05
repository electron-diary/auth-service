from enum import Enum
from typing import Self


class ErrorType(Enum):
    INVALID_CONTACTS = "invalid_contacts"
    INVALID_AGE = "invalid_age"
    INVALID_NAME = "invalid_name"
    INVALID_GENDER = "invalid_gender"
    INVALID_ID = "invalid_id"
    INVALID_STATUS = "invalid_status"
    INVALID_PICTURES = "invalid_pictures"
    INVALID_ADDRESS = "invalid_address"


class DomainError(Exception):
    def __init__(
        self: Self,
        data: str,
        exc: ErrorType,
    ) -> None:
        super().__init__(data)

        self.data: str = data
        self.exc: ErrorType = exc
