from typing import Self
from dataclasses import dataclass

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError
        
@dataclass(frozen=True)
class UserContact(DomainValueObject[str | int]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User contact cannot be empty"
            )
        if not isinstance(self.to_raw(), (str, int)):
            raise DomainValidationError(
                "User contact must be a string or an integer"
            )
        if isinstance(self.to_raw(), str) and len(self.object) > 20:
            raise DomainValidationError(
                "User contact must be less than 20 characters long"
            )

