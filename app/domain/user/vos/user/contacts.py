from typing import Self


class Contacts:
    def __init__(
        self: Self,
        phone: int | None,
        email: str | None,
    ) -> None:
        self.phone: int | None = phone
        self.email: str | None = email

        self.validate()

    def validate(self: Self) -> None:
        if self.phone is None and self.email is None:
            raise ValueError("Phone and email cannot be None at the same time")

        if self.phone and not isinstance(self.phone, int):
            raise ValueError("Phone must be an integer")

        if self.email and not isinstance(self.email, str):
            raise ValueError("Email must be a string")
