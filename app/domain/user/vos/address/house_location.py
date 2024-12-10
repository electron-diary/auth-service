from typing import Self


class HouseNumber:
    def __init__(
        self: Self,
        value: str,
    ) -> None:
        self.value: str = value

        self.validate()

    def validate(self: Self,) -> None:
        if not self.value:
            raise ValueError('House number cannot be empty')

        if not isinstance(self.value, str):
            raise ValueError('House number must be a string')

        