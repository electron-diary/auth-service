from dataclasses import dataclass

from app.domain.common.common_event import CommonDomainEvent
from app.domain.constants.user_contact import UserContact
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class UpdateUserContactEvent(CommonDomainEvent[UUIDValueObject, TimestampValueObject]):
    user_uuid: UUIDValueObject
    new_user_contact: UserContact
    user_updated_at: TimestampValueObject
