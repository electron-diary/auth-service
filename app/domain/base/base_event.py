from dataclasses import dataclass, field

from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class BaseDomainEvent:
    event_uuid: UUIDValueObject = field(default=UUIDValueObject.set_default(), init=False)
    event_start_execution_time: TimestampValueObject = field(default=TimestampValueObject.set_default(), init=False)
