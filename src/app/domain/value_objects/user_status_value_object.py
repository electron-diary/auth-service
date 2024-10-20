from typing import Self
from dataclasses import dataclass

from src.app.domain.common.value_objects import DomainValueObject
from src.app.domain.common.exceptions import DomainValidationError
        
@dataclass(frozen=True)
class UserStatus(DomainValueObject[bool]):
    def validate(self: Self) -> None:
        if self.to_raw() is None:
            raise DomainValidationError(
                "User status cannot be empty"
            )
        if not isinstance(self.to_raw(), bool):
            raise DomainValidationError(
                "User status must be a boolean"
            )

