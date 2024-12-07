from typing import Self

from app.domain.user.exceptions import UserError, ErrorType


class Fullname:
    def __init__(
        self: Self,
        first_name: str,
        last_name: str,
        middle_name: str | None = None,
    ) -> None:
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.middle_name: str | None = middle_name

        self.to_raw()

    def to_raw(self: Self) -> None:
        if not self.first_name or not isinstance(self.first_name, str):
            raise UserError("Invalid firstname", ErrorType.INVALID_NAME)

        if not self.last_name or not isinstance(self.last_name, str):
            raise UserError("Invalid lastname", ErrorType.INVALID_NAME)

        if self.middle_name and not isinstance(self.middle_name, str):
            raise UserError("Invalid middlename", ErrorType.INVALID_NAME)

