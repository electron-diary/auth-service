from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidFirstNameException


@dataclass(frozen=True)
class FirstNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise InvalidFirstNameException(
                message="First name must not be empty",
            )
        if not isinstance(self.to_raw(), str):
            raise InvalidFirstNameException(
                message=f"First name must be a string, not {type(self.to_raw())}",
            )
        if len(self.to_raw()) > ...:
            raise InvalidFirstNameException(
                message=f"First name must be less than {...} characters",
            )
        if len(self.to_raw()) < ...:
            raise InvalidFirstNameException(
                message=f"First name must be greater than {...} characters",
            )
