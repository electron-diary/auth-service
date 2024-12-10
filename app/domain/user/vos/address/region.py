from typing import Self


class Region:
    def __init__(
        self: Self,
        value: str,
    ) -> None:
        self.value: str = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Region cannot be empty")

        if not isinstance(self.value, str):
            raise TypeError("Region must be a string")
