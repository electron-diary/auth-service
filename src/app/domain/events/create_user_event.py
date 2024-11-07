from dataclasses import dataclass

from app.domain.common.common_event import CommonDomainEvent
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_name_value_object import UserNameValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass(frozen=True)
class CreateUserEvent(CommonDomainEvent[UUIDValueObject, TimestampValueObject]):
    user_uuid: UUIDValueObject
    user_name: UserNameValueObject
    user_email: UserEmailValueObject
    user_phone: UserPhoneValueObject
    user_created_at: TimestampValueObject
    user_updated_at: TimestampValueObject
