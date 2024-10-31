from typing import Self
from dataclasses import dataclass
from uuid import UUID

from app.domain.common.value_objects import DomainValueObject
from app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class UserUUID(DomainValueObject[UUID]):
    def validate(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "User UUID cannot be empty"
            )
        if not isinstance(self.object, UUID):
            raise DomainValidationError(
                "User UUID must be a valid UUID"
            )
        
