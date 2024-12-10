from typing import Self

from app.domain.user.enums.statuses import ProfileStatus


class Status:
    def __init__(
        self: Self,
        value: ProfileStatus = ProfileStatus.ACTIVE,
    ) -> None:
        self.value: ProfileStatus = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Status is required")

        if not isinstance(self.value, ProfileStatus):
            raise ValueError("Invalid status")

        if self.value not in list(ProfileStatus):
            raise ValueError("Invalid status")
