from dataclasses import dataclass

from app.domain.common.common_event import CommonDomainEvent
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.user_first_name_value_object import UserNameValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class UpdateUserNameEvent(CommonDomainEvent[UUIDValueObject, TimestampValueObject]):
    user_uuid: UUIDValueObject
    new_user_name: UserNameValueObject
    user_updated_at: TimestampValueObject
