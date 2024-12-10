from typing import Self

from app.domain.user.enums.genders import Genders


class Gender:
    def __init__(
        self: Self,
        value: Genders | None,
    ) -> None:
        self.value: Genders | None = value

        self.validate()

    def validate(self: Self) -> None:
        if self.value and not isinstance(self.value, Genders):
            raise ValueError("Invalid gender")

        if self.value and self.value not in list(Genders):
            raise ValueError("Invalid gender")
