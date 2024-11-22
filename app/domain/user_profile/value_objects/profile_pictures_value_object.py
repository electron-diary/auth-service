from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidProfilePictureException


@dataclass(frozen=True)
class ProfilePucturesValueObject(CommonDomainValueObject):
    profile_pictures: list[str] | None

    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.profile_pictures, list):
                raise InvalidProfilePictureException(
                    message=f"Profile pictures must be a list of strings, not {type(self.profile_pictures)}",
                )
            for item in self.profile_pictures:
                if not isinstance(item, str):
                    raise InvalidProfilePictureException(
                        message=f"Profile picture must be a string, not {type(item)}",
                    )

