from typing import Self

from app.domain.user.exceptions import UserError, ErrorType
from app.domain.user.enums.gender import GenderTypes


class Gender:
    def __init__(
        self: Self,
        gender: GenderTypes | None = None,
    ) -> None:
        self.gender: GenderTypes | None = gender

        self.to_raw()

    def to_raw(self: Self) -> None:
        if self.gender and not isinstance(self.gender, GenderTypes):
            raise UserError("Invalid gender", ErrorType.INVALID_GENDER)

        if self.gender and self.gender not in list(GenderTypes):
            raise UserError("Invalid gender", ErrorType.INVALID_GENDER)
