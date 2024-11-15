from dataclasses import dataclass

from app.domain.base.base_event import BaseDomainEvent
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class DeleteUserEvent(BaseDomainEvent):
    user_uuid: UUIDValueObject
