from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.domain.user.exceptions import UserException


@dataclass(frozen=True)
class UserId:
    value: UUID

    def __post_init__(self: Self) -> None:
        if not self.value:
            raise UserException("UserId cannot be empty")
        if not UUID(str(self.value)):
            raise UserException(f"UserId must be a UUID, not {type(self.value)}")

@dataclass(frozen=True)
class Username:
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
    phone: int

    def __post_init__(self: Self) -> None:
        if not self.phone:
            raise UserException("Phone cannot be empty")
        if not isinstance(self.phone, int):
            raise UserException(f"Phone must be a int, not {type(self.phone)}")

@dataclass(frozen=True)
class DeletedUser:
    value: bool

    def __post_init__(self: Self) -> None:
        if self.value is None:
            raise UserException("DeleteUser cannot be None")
