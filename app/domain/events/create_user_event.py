from dataclasses import dataclass, field

from app.domain.common.common_event import CommonDomainEvent
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class CreateUserEvent(CommonDomainEvent):
    user_uuid: UUIDValueObject
    user_contact: UserContact
    user_fullname: UserFullName
    user_created_at: TimestampValueObject = field(default=TimestampValueObject.set_default(), init=False)
    user_updated_at: TimestampValueObject = field(default=TimestampValueObject.set_default(), init=False)
