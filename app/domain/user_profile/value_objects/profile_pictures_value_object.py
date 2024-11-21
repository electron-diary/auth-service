from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidProfilePictureException


@dataclass(frozen=True)
class ProfilePucturesValueObject(CommonDomainValueObject[list[str] | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), list):
                raise InvalidProfilePictureException(
                    message=f"Profile pictures must be a list of strings, not {type(self.to_raw())}",
                )
            for item in self.to_raw():
                if not isinstance(item, str):
                    raise InvalidProfilePictureException(
                        message=f"Profile picture must be a string, not {type(item)}",
                    )

