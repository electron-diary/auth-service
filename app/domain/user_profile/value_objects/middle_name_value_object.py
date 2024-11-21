from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidMiddleNameException


@dataclass(frozen=True)
class MiddleNameValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise InvalidMiddleNameException(
                    message=f"Middle name must be a string, not {type(self.to_raw())}",
                )
            if len(self.to_raw()) > ...:
                raise InvalidMiddleNameException(
                    message=f"Middle name must be less than {...} characters",
                )
            if len(self.to_raw()) < ...:
                raise InvalidMiddleNameException(
                    message=f"Middle name must be more than {...} characters",
                )
