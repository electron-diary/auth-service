from typing import Self


class Username:
    def __init__(
        self: Self,
        value: str,
    ) -> None:
        self.value: str = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Username cannot be empty")

        if not isinstance(self.value, str):
            raise TypeError("Username must be a string")
