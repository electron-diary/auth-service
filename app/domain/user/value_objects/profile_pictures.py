from typing import Self

from app.domain.user.exceptions import DomainError, ErrorType


class ProfilePictures:
    def __init__(
        self: Self,
        profile_pictures: list[str],
    ) -> None:
        self.profile_pictures: list[str] = profile_pictures

        self.to_raw()

    def to_raw(self: Self) -> None:
        if not isinstance(self.profile_pictures, list):
            raise DomainError("Invalid pictures", ErrorType.INVALID_PICTURES)

        for picture in self.profile_pictures:
            if not isinstance(picture, str):
                raise DomainError("Invalid pictures", ErrorType.INVALID_PICTURES)
