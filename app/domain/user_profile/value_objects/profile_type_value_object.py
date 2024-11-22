from dataclasses import dataclass
from typing import Literal, Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidProfileTypeException

ProfileT = Literal["verified", "unverified"]


@dataclass(frozen=True)
class ProfileTypeValueObject(CommonDomainValueObject):
    profile_type: ProfileT

    def __post_init__(self: Self) -> None:
        if not self.profile_type:
            raise InvalidProfileTypeException(
                message="Profile type must not be None",
            )
        if not isinstance(self.profile_type, str):
            raise InvalidProfileTypeException(
                message=f"Profile type must be a string, not {type(self.profile_type)}",
            )

        if self.profile_type not in ["verified", "unverified"]:
            raise InvalidProfileTypeException(
                message="Profile type must be either 'verified' or 'unverified'",
            )
