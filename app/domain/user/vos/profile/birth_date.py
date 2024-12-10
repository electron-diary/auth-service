from datetime import date
from typing import Self


class BirthDate:
    def __init__(
        self: Self,
        value: date | None,
    ) -> None:
        self.value: date | None = value

        self.validate()

    def validate(self: Self) -> None:
        if self.value and not isinstance(self.value, date):
            raise ValueError("Birth date must be a date")

        if self.value and self.value > date.today():
            raise ValueError("Birth date cannot be in the future")
