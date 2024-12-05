from typing import Self

from app.domain.user.exceptions import DomainError, ErrorType


class Age:
    def __init__(
        self: Self,
        age: int | None = None,
    ) -> None:
        self.age: int | None = age

        self.to_raw()

    def to_raw(self: Self) -> None:
        if self.age and  not isinstance(self.age, int):
            raise DomainError("Invalid age", ErrorType.INVALID_AGE)

        if self.age and self.age < 0:
            raise DomainError("Invalid age", ErrorType.INVALID_AGE)
