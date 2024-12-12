from typing import Self

from app.domain.models.user.exceptions import ErrorType, UserException


class Contacts:
    def __init__(
        self: Self, 
        phone_number: int | None,
        email: str | None,
    ) -> None:
        self.phone_number = phone_number
        self.email = email

        self.validate()

    def validate(self: Self) -> None:
        if self.phone_number is None and self.email is None:
            raise UserException(ErrorType.INVALID_CONTACTS, "At least one contact must be provided")
        
        if self.phone_number and not isinstance(self.phone_number, int):
            raise UserException(ErrorType.INVALID_CONTACTS, "Phone number must be an integer")
        
        if self.email and not isinstance(self.email, str):
            raise UserException(ErrorType.INVALID_CONTACTS, "Email must be a string")
        
    def __str__(self: Self) -> str:
        if self.phone_number and self.email:
            return f"{self.phone_number} {self.email}"

        if self.phone_number:
            return f"{self.phone_number}"

        return f"{self.email}"
        