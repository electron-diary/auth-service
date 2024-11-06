from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserPhoneValueObject(CommonDomainValueObject[int | None]):
    def validate(self: Self) -> None:
        if not isinstance(self.to_raw(), (int, None)):
            raise DomainValidationError(
                "User phone must be an integer or None",
            )
        if isinstance(self.to_raw(), int) and len(str(self.to_raw())) > 20:
            raise DomainValidationError(
                "User phone must be less than 20 characters long",
            )
