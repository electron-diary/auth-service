from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserPhoneValueObject(CommonDomainValueObject[int | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), int):
                raise DomainValidationError(
                    "User phone must be an integer",
                )
            if len(str(self.to_raw())) > 20:
                raise DomainValidationError(
                    "User phone must be less than 20 characters long",
                )
        
