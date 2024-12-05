from typing import Self

from app.domain.user.exceptions import DomainError, ErrorType


class Contacts:
    def __init__(
        self: Self,
        phone_number: int | None = None,
        email: str | None = None,
    ) -> None:
        self.phone_number: int | None = phone_number
        self.email: str | None = email

        self.to_raw()

    def to_raw(self: Self) -> None:
        if not self.phone_number and not self.email:
            raise DomainError("Invalid contacts", ErrorType.INVALID_CONTACTS)

        if self.phone_number and not isinstance(self.phone_number, int):
            raise DomainError("Invalid phone number", ErrorType.INVALID_CONTACTS)

        if self.email and not isinstance(self.email, str):
            raise DomainError("Invalid email", ErrorType.INVALID_CONTACTS)
