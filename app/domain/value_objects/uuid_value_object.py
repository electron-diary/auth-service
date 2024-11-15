from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4

from app.domain.exceptions.value_objects_exceptions import UUIDRequiredError
from app.domain.exceptions.value_objects_exceptions import UUIDTypeError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class UUIDValueObject(CommonDomainValueObject[UUID]):
    @staticmethod
    def set_default() -> 'UUIDValueObject':
        return UUIDValueObject(uuid4())

    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise UUIDRequiredError(
                "UUID cannot be empty",
            )
        if not isinstance(self.object, UUID):
            raise UUIDTypeError(
                "UUID must be a valid UUID",
            )
