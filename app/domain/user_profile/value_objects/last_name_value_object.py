from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidLastNameException


@dataclass(frozen=True)
class LastNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise InvalidLastNameException(
                message="Last name cannot be empty",
            )
        if not isinstance(self.to_raw(), str):
            raise InvalidLastNameException(
                message=f"Last name must be a string, not {type(self.to_raw())}",
            )
        if len(self.to_raw()) > ...:
            raise InvalidLastNameException(
                message=f"Last name must be less than {...} characters",
            )
        if len(self.to_raw()) < ...:
            raise InvalidLastNameException(
                message=f"Last name must be greater than {...} characters",
            )
