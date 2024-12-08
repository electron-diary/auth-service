from typing import Self

from app.domain.user.enums.statuses import StatusTypes
from app.domain.user.exceptions import ErrorType, UserError


class Status:
    def __init__(
        self: Self,
        status: StatusTypes = StatusTypes.ACTIVE,
    ) -> None:
        self.status: StatusTypes = status

        self.to_raw()

    def to_raw(self: Self) -> None:
        if not self.status or not isinstance(self.status, StatusTypes):
            raise UserError("Invalid user status", ErrorType.INVALID_STATUS)

        if self.status not in list(StatusTypes):
            raise UserError("Invalid user status", ErrorType.INVALID_STATUS)
