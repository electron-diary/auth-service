from typing import Self

from app.domain.user.enums.roles import ProfileTypes


class ProfileType:
    def __init__(
        self: Self,
        value: ProfileTypes = ProfileTypes.STUDENT,
    ) -> None:
        self.value: ProfileType = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Profile type is required")

        if not isinstance(self.value, ProfileTypes):
            raise ValueError("Invalid profile type")

        if self.value not in list(ProfileTypes):
            raise ValueError("Invalid profile type")
