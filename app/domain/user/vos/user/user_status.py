from typing import Self

from app.domain.user.enums.statuses import UserStatus


class Status:
    def __init__(
        self: Self,
        value: UserStatus = UserStatus.ACTIVE,
    ) -> None:
        self.value: UserStatus = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Status is required")

        if not isinstance(self.value, UserStatus):
            raise ValueError("Invalid status")

        if self.value not in list(UserStatus):
            raise ValueError("Invalid status")


