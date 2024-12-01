from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.domain.user.exceptions import UserException


@dataclass(frozen=True)
class UserId:
    """
    Value object representing a user's unique identifier.
    Ensures the ID is a valid UUID and not empty.

    Attributes:
        value (UUID): The UUID value for the user ID

    Raises:
        UserException: If the ID is empty or not a valid UUID
    """

    value: UUID

    def __post_init__(self: Self) -> None:
        if not self.value:
            raise UserException("UserId cannot be empty")
        if not UUID(str(self.value)):
            raise UserException(f"UserId must be a UUID, not {type(self.value)}")


@dataclass(frozen=True)
class Username:
    """
    Value object representing a user's display name.
    Enforces username format rules and validation.

    Attributes:
        value (str): The username string

    Raises:
        UserException: If the username is:
            - Empty
            - Not a string
            - Shorter than 3 characters
            - Longer than 20 characters
    """

    value: str

    def __post_init__(self: Self) -> None:
        if not self.value:
            raise UserException("Username cannot be empty")
        if not isinstance(self.value, str):
            raise UserException(f"Username must be a string, not {type(self.value)}")
        if len(self.value) < 3:
            raise UserException("Username must be at least 3 characters long")
        if len(self.value) > 20:
            raise UserException("Username must be at most 20 characters long")


@dataclass(frozen=True)
class Contacts:
    """
    Value object representing user's contact information.
    Currently handles phone number validation.

    Attributes:
        phone (int): The user's phone number

    Raises:
        UserException: If the phone number is:
            - Empty
            - Not an integer
    """

    phone: int

    def __post_init__(self: Self) -> None:
        if not self.phone:
            raise UserException("Phone cannot be empty")
        if not isinstance(self.phone, int):
            raise UserException(f"Phone must be a int, not {type(self.phone)}")


@dataclass(frozen=True)
class DeletedUser:
    """
    Value object representing user's deletion status.
    Ensures the deletion flag is properly set.

    Attributes:
        value (bool): Flag indicating if the user is deleted

    Raises:
        UserException: If the deletion status is None
    """

    value: bool

    def __post_init__(self: Self) -> None:
        if self.value is None:
            raise UserException("DeleteUser cannot be None")
