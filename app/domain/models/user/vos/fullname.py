from typing import Self


class Fullname:
    def __init__(
        self: Self,
        first_name: str,
        last_name: str,
        middle_name: str | None,
    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

        self.validate()

    def validate(self: Self) -> None:
        if not isinstance(self.first_name, str):
            raise Exception("First name must be a string")

        if not isinstance(self.last_name, str):
            raise Exception("Last name must be a string")

        if self.middle_name and not isinstance(self.middle_name, str):
            raise Exception("Middle name must be a string")

        if not self.first_name or not self.last_name:
            raise Exception("First name and last name must be provided")
        
    def __str__(self: Self) -> str:
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

        return f"{self.first_name} {self.last_name}"