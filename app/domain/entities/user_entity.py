from dataclasses import dataclass, field
from datetime import datetime
from typing import Self

from app.domain.common.common_entity import CommonDomainEntity
from app.domain.common.agregate_root import AgregateRoot
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.value_objects.timestamp_value_object import TimestampValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass
class UserDomainEntity(CommonDomainEntity[UUIDValueObject], AgregateRoot):
    user_full_name: UserFullName
    user_contact: UserContact
    user_created_at: TimestampValueObject = field(default=TimestampValueObject.set_default())
    user_updated_at: TimestampValueObject = field(default=TimestampValueObject.set_default())
    
    @staticmethod
    def create_user(
        user_uuid: UUIDValueObject, 
        user_contact: UserContact, user_fullname: UserFullName
    ) -> 'UserDomainEntity':
        user_entity: UserDomainEntity = UserDomainEntity(
            user_uuid=user_uuid,
            user_contact=user_contact,
            user_full_name=user_fullname,
        )
        event: CreateUserEvent = CreateUserEvent(
            user_uuid=user_entity.user_uuid,
            user_contact=user_entity.self.user_contact,
            user_fullname=user_entity.user_fullname,
        )
        user_entity.add_event(event=event)
        return user_entity

    def update_user_fullname(
        self: Self, user_uuid: UUIDValueObject, new_user_fullname: UserFullName,
    ) -> None:
        event: UpdateUserFullNameEvent = UpdateUserFullNameEvent(
            new_user_fullname=new_user_fullname,
            user_uuid=user_uuid,
        )
        self.add_event(event=event)

    def update_user_contact(
        self: Self, user_uuid: UUIDValueObject, new_user_contact: UserContact,
    ) -> None:
        event: UpdateUserContactEvent = UpdateUserContactEvent(
            new_user_contact=new_user_contact,
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

