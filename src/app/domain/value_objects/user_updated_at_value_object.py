from typing import Self
from dataclasses import dataclass
from datetime import datetime

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class UserUpdatedAt(DomainValueObject[datetime]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User updated at cannot be empty"
            )
        if not isinstance(self.to_raw(), datetime):
            raise DomainValidationError(
                "User updated at must be a datetime"
            )

        
