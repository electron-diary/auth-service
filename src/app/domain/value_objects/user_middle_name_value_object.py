from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserMiddleNameValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise DomainValidationError(
                    "User middle name must be a string",
                )
            if len(self.to_raw()) < 3:
                raise DomainValidationError(
                    "User middle name must be at least 3 characters long",
                )
            if len(self.to_raw()) > 20:
                raise DomainValidationError(
                    "User middle name must be less than 50 characters long",
                )
