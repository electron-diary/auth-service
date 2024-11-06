from dataclasses import dataclass
from datetime import datetime
from typing import Self

from app.domain.common.common_entity import CommonDomainEntity
from app.domain.common.common_exceptions import DomainValidationError
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_email_event import UpdateUserEmailEvent
from app.domain.events.update_user_name_event import UpdateUserNameEvent
from app.domain.events.update_user_phone_event import UpdateUserPhoneEvent
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_name_value_object import UserNameValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass
class UserDomainEntity(CommonDomainEntity[UUIDValueObject]):
    user_name: UserNameValueObject
    user_email: UserEmailValueObject
    user_phone: UserPhoneValueObject
    user_created_at: TimestampValueObject
    user_updated_at: TimestampValueObject

    def create_user(
        self: Self,
        user_uuid: UUIDValueObject,
        user_email: UserEmailValueObject,
        user_phone: UserPhoneValueObject,
        user_name: UserNameValueObject,
    ) -> CreateUserEvent:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: CreateUserEvent = CreateUserEvent(
            user_uuid=user_uuid,
            user_email=user_email,
            user_phone=user_phone,
            user_name=user_name,
            user_created_at=timestamp_value_object,
            user_updated_at=timestamp_value_object,
        )

        return event

    def update_user_email(self: Self, user_uuid: UUIDValueObject, user_email: UserEmailValueObject) -> UpdateUserEmailEvent:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: UpdateUserEmailEvent = UpdateUserEmailEvent(
            new_user_email=user_email,
            user_updated_at=timestamp_value_object,
            user_uuid=user_uuid,
        )

        return event

    def update_user_name(self: Self, user_uuid: UUIDValueObject, new_user_name: UserNameValueObject) -> UpdateUserNameEvent:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: UpdateUserNameEvent = UpdateUserNameEvent(
            new_user_name=new_user_name,
            user_updated_at=timestamp_value_object,
            user_uuid=user_uuid,
        )

        return event

    def update_user_phone(self: Self, user_uuid: UUIDValueObject, user_phone: UserPhoneValueObject) -> UpdateUserPhoneEvent:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: UpdateUserPhoneEvent = UpdateUserPhoneEvent(
            new_user_phone=user_phone,
            user_updated_at=timestamp_value_object,
            user_uuid=user_uuid,
        )

        return event

    def delete_user(self: Self, user_uuid: UUIDValueObject) -> DeleteUserEvent:
        event: DeleteUserEvent = DeleteUserEvent(
            user_uuid=user_uuid,
        )

        return event

    def __post_init__(self: Self) -> None:
        if self.user_email.to_raw() is None and self.user_phone.to_raw() is None:
            raise DomainValidationError(
                "User must have at least one contact information",
            )

