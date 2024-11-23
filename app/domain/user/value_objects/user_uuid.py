from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import InvalidUuidException


@dataclass(frozen=True)
class UserUUID(CommonDomainValueObject[UUID]):
    id: UUID

    def __post_init__(self: Self) -> None:
        if not self.id:
            raise InvalidUuidException(
                message="User UUID cannot be empty",
            )
        if not isinstance(self.id, UUID):
            raise InvalidUuidException(
                message=f"User UUID must be a UUID, not {type(self.id)}",
            )
