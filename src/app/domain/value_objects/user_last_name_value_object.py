from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserLastNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User last name cannot be empty",
            )
        if not isinstance(self.to_raw(), str):
            raise DomainValidationError(
                "User last name must be a string",
            )
        if len(self.to_raw()) < 3:
            raise DomainValidationError(
                "User last name must be at least 3 characters long",
            )
        if len(self.to_raw()) > 20:
            raise DomainValidationError(
                "User last name must be less than 50 characters long",
            )
