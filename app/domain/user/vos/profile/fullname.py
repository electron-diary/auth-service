from typing import Self


class Fullname:
    def __init__(
        self: Self,
        firstname: str,
        lastname: str,
        middlename: str | None = None,
    ) -> None:
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.middlename: str | None = middlename

        self.validate()

    def validate(self: Self) -> None:
        if not self.firstname:
            raise ValueError("Firstname cannot be empty")

        if not isinstance(self.firstname, str):
            raise TypeError("Firstname must be a string")

        if not self.lastname:
            raise ValueError("Lastname cannot be empty")

        if not isinstance(self.lastname, str):
            raise TypeError("Lastname must be a string")

        if self.middlename and not isinstance(self.middlename, str):
            raise TypeError("Middlename must be a string")
