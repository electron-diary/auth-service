from dataclasses import dataclass

from app.domain.common.common_event import CommonDomainEvent
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class UpdateUserPhoneEvent(CommonDomainEvent[UUIDValueObject, TimestampValueObject]):
    user_uuid: UUIDValueObject
    new_user_phone: UserPhoneValueObject
    user_updated_at: TimestampValueObject
