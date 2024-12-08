from typing import Self
from uuid import UUID

from app.domain.user.exceptions import ErrorType, UserError


class Id:
    def __init__(
        self: Self,
        id: UUID,
    ) -> None:
        self.id: UUID = id

        self.to_raw()

    def to_raw(self: Self) -> None:
        if not self.id or not isinstance(self.id, UUID):
            raise UserError("Invalid id", ErrorType.INVALID_ID)
