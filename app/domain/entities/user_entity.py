from dataclasses import dataclass
from typing import Self

from app.domain.base.agregate_root import AgregateRoot
from app.domain.base.base_entity import BaseDomainEntity
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass
class UserDomainEntity(BaseDomainEntity[UUIDValueObject], AgregateRoot):
    user_full_name: UserFullName
    user_contact: UserContact

    @staticmethod
    def create_user(
        user_uuid: UUIDValueObject,
        user_contact: UserContact, user_fullname: UserFullName,
    ) -> "UserDomainEntity":
        user_entity: UserDomainEntity = UserDomainEntity(
            user_uuid=user_uuid,
            user_contact=user_contact,
            user_full_name=user_fullname,
        )
        event: CreateUserEvent = CreateUserEvent(
            user_uuid=user_entity.user_uuid.to_raw(),
            user_email=user_entity.user_contact.user_email.to_raw(),
            user_phone=user_entity.user_contact.user_phone.to_raw(),
            user_first_name=user_entity.user_full_name.user_first_name.to_raw(),
            user_middle_name=user_entity.user_full_name.user_middle_name.to_raw(),
            user_last_name=user_entity.user_full_name.user_last_name.to_raw(),
        )
        user_entity.add_event(event=event)
        return user_entity

    def update_user_fullname(
        self: Self, user_uuid: UUIDValueObject, new_user_fullname: UserFullName,
    ) -> None:
        event: UpdateUserFullNameEvent = UpdateUserFullNameEvent(
            user_uuid=user_uuid.to_raw(),
            new_user_first_name=new_user_fullname.user_first_name.to_raw(),
            new_user_middle_name=new_user_fullname.user_middle_name.to_raw(),
            new_user_last_name=new_user_fullname.user_last_name.to_raw(),
        )
        self.add_event(event=event)

    def update_user_contact(
        self: Self, user_uuid: UUIDValueObject, new_user_contact: UserContact,
    ) -> None:
        event: UpdateUserContactEvent = UpdateUserContactEvent(
            user_uuid=user_uuid.to_raw(),
            new_user_email=new_user_contact.user_email.to_raw(),
            new_user_phone=new_user_contact.user_phone.to_raw(),
        )
        self.add_event(event=event)

    def delete_user(
        self: Self, user_uuid: UUIDValueObject,
    ) -> None:
        event: DeleteUserEvent = DeleteUserEvent(
            user_uuid=user_uuid.to_raw(),
        )
        self.add_event(event=event)

