from typing import Self


class Bio:
    def __init__(
        self: Self,
        value: str | None
    ) -> None:
        self.value: str | None = value

        self.validate()

    def validate(self: Self) -> None:
        if self.value and not isinstance(self.value, str):
            raise TypeError('Bio must be a string')

        if self.value and len(self.value) > 1000:
            raise ValueError('Bio must be less than 1000 characters')