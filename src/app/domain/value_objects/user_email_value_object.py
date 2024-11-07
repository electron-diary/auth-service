from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UserEmailValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if not isinstance(self.to_raw(), (str, None)):
            raise DomainValidationError(
                "User email must be an integer or None",
            )
        if isinstance(self.to_raw(), str) and len(self.to_raw()) > 30:
            raise DomainValidationError(
                "User email must be less than 20 characters long",
            )
