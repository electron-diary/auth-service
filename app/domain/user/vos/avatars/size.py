from typing import Self


class FileSize:
    def __init__(
        self: Self,
        value: int,
    ) -> None:
        self.value: int = value

        self.validate()

    def validate(self: Self) -> None:
        if not isinstance(self.value, int):
            raise TypeError('File size must be an integer')

        if self.value < 0:
            raise ValueError('File size must be a positive integer')