from dataclasses import dataclass, field

from app.domain.base.base_event import BaseDomainEvent
from app.domain.constants.user_fullname import UserFullName
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class UpdateUserFullNameEvent(BaseDomainEvent):
    user_uuid: UUIDValueObject
    new_user_fullname: UserFullName
    user_updated_at: TimestampValueObject = field(default=TimestampValueObject.set_default(), init=False)
