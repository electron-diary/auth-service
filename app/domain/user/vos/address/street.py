from typing import Self


class Street:
    def __init__(
        self: Self,
        value: str
    ) -> None:
        self.value: str = value

        self.validate()

    def validate(self: Self) -> None:
        if not isinstance(self.value, str):
            raise TypeError('Street value must be a string')

        if not self.value:
            raise ValueError('Street value must not be empty')