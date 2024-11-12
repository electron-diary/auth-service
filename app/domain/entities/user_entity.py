from dataclasses import dataclass
from datetime import datetime
from typing import Self

from app.domain.common.common_entity import CommonDomainEntity
from app.domain.common.common_events_agregator import EventsAgregator
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass
class UserDomainEntity(CommonDomainEntity[UUIDValueObject], EventsAgregator):
    user_full_name: UserFullName
    user_contact: UserContact
    user_created_at: TimestampValueObject
    user_updated_at: TimestampValueObject
    
    def create_user(
        self: Self,
        user_uuid: UUIDValueObject,
        user_contact: UserContact,
        user_fullname: UserFullName,
    ) -> None:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: CreateUserEvent = CreateUserEvent(
            user_uuid=user_uuid,
            user_contact=user_contact,
            user_fullname=user_fullname,
            user_created_at=timestamp_value_object,
            user_updated_at=timestamp_value_object,
        )
        self.add_event(event=event)

    def update_user_fullname(
        self: Self, user_uuid: UUIDValueObject, new_user_fullname: UserFullName,
    ) -> None:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: UpdateUserFullNameEvent = UpdateUserFullNameEvent(
            new_user_fullname=new_user_fullname,
            user_updated_at=timestamp_value_object,
            user_uuid=user_uuid,
        )
        self.add_event(event=event)

    def update_user_contact(
        self: Self, user_uuid: UUIDValueObject, new_user_contact: UserContact,
    ) -> None:
        timestamp: datetime = datetime.now()
        timestamp_value_object: TimestampValueObject = TimestampValueObject(timestamp)
        event: UpdateUserContactEvent = UpdateUserContactEvent(
            new_user_contact=new_user_contact,
            user_updated_at=timestamp_value_object,
            user_uuid=user_uuid,
        )
        self.add_event(event=event)
    
    def delete_user(
        self: Self, user_uuid: UUIDValueObject,
    ) -> None:
        event: DeleteUserEvent = DeleteUserEvent(
            user_uuid=user_uuid,
        )
        self.add_event(event=event)

