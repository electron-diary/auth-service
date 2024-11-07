from dataclasses import dataclass
from datetime import datetime
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class TimestampValueObject(CommonDomainValueObject[datetime]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User updated at cannot be empty",
            )
        if not isinstance(self.to_raw(), datetime):
            raise DomainValidationError(
                "User updated at must be a datetime",
            )
