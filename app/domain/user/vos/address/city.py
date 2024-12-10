from typing import Self


class City:
    def __init__(
        self: Self,
        value: str
    ) -> None:
        self.value: str = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError('City cannot be empty')
        
        if not isinstance(self.value, str):
            raise TypeError('City must be a string')