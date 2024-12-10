from typing import Self


class FileName:
    def __init__(
        self: Self,
        value: str
    ) -> None:
        self.value: str = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError('File name must not be empty')
        
        if not isinstance(self.value, str):
            raise TypeError('File name must be a string')
