from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.domain.base.domain_vo import DomainVO
from app.domain.user.exceptions import UserException


@dataclass(frozen=True)
class UserId(DomainVO):
    value: UUID

    def __post_init__(self: Self) -> None:
        if not self.value:
            raise UserException("UserId cannot be empty")
        if not UUID(str(self.value)):
            raise UserException(f"UserId must be a UUID, not {type(self.value)}")

@dataclass(frozen=True)
class Username(DomainVO):
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
class Contacts(DomainVO):
    email: str | None
    phone: int | None

    def __post_init__(self: Self) -> None:
        if self.email is not None and not isinstance(self.email, str):
            raise UserException(f"Email must be a string, not {type(self.email)}")
        if self.phone is not None and not isinstance(self.phone, int):
            raise UserException(f"Phone must be an integer, not {type(self.phone)}")

@dataclass(frozen=True)
class DeletedUser(DomainVO):
    value: bool

    def __post_init__(self: Self) -> None:
        if self.value is None:
            raise UserException("DeleteUser cannot be None")
