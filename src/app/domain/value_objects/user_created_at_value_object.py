from typing import Self
from dataclasses import dataclass
from datetime import datetime

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class UserCreatedAt(DomainValueObject[datetime]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User created at cannot be empty"
            )
        if not isinstance(self.to_raw(), datetime):
            raise DomainValidationError(
                "User created at must be a datetime"
            )
    

        
