from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UUIDValueObject(CommonDomainValueObject[UUID]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise DomainValidationError(
                "UUID cannot be empty",
            )
        if not isinstance(self.object, UUID):
            raise DomainValidationError(
                "UUID must be a valid UUID",
            )
