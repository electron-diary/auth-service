from dataclasses import dataclass
from typing import Self

from app.domain.base.agregate_root import AgregateRoot
from app.domain.base.base_entity import BaseDomainEntity
from app.domain.base.base_event import BaseDomainEvent
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.exceptions.events_exception import EventsConsistencyError
from app.domain.exceptions.user_exceptions import UserDeletedError
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_first_name_value_object import UserFirstNameValueObject
from app.domain.value_objects.user_last_name_value_object import UserLastNameValueObject
from app.domain.value_objects.user_middle_name_value_object import UserMiddleNameValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


@dataclass
class UserDomainEntity(BaseDomainEntity[UUIDValueObject], AgregateRoot):
    user_full_name: UserFullName
    user_contact: UserContact

    @staticmethod
    def create_user(
        uuid: UUIDValueObject,
        user_contact: UserContact, user_fullname: UserFullName,
    ) -> "UserDomainEntity":
        user_entity: UserDomainEntity = UserDomainEntity(
            uuid=uuid,
            user_contact=user_contact,
            user_full_name=user_fullname,
        )
        event: CreateUserEvent = CreateUserEvent(
            uuid=user_entity.uuid.to_raw(),
            user_email=user_entity.user_contact.user_email.to_raw(),
            user_phone=user_entity.user_contact.user_phone.to_raw(),
            user_first_name=user_entity.user_full_name.user_first_name.to_raw(),
            user_middle_name=user_entity.user_full_name.user_middle_name.to_raw(),
            user_last_name=user_entity.user_full_name.user_last_name.to_raw(),
        )
        user_entity.add_event(event=event)
        return user_entity

    def update_user_fullname(
        self: Self, uuid: UUIDValueObject, new_user_fullname: UserFullName,
    ) -> None:
        event: UpdateUserFullNameEvent = UpdateUserFullNameEvent(
            uuid=uuid.to_raw(),
            new_user_first_name=new_user_fullname.user_first_name.to_raw(),
            new_user_middle_name=new_user_fullname.user_middle_name.to_raw(),
            new_user_last_name=new_user_fullname.user_last_name.to_raw(),
        )
        self._apply(event=event)
        self.add_event(event=event)

    def update_user_contact(
        self: Self, uuid: UUIDValueObject, new_user_contact: UserContact,
    ) -> None:
        event: UpdateUserContactEvent = UpdateUserContactEvent(
            uuid=uuid.to_raw(),
            new_user_email=new_user_contact.user_email.to_raw(),
            new_user_phone=new_user_contact.user_phone.to_raw(),
        )
        self._apply(event=event)
        self.add_event(event=event)

    def delete_user(
        self: Self, uuid: UUIDValueObject,
    ) -> None:
        event: DeleteUserEvent = DeleteUserEvent(
            uuid=uuid.to_raw(),
        )
        self._apply(event=event)
        self.add_event(event=event)

    def _apply(self: Self, event: BaseDomainEvent) -> None:
        if isinstance(event, DeleteUserEvent):
            msg = "User already deleted"
            raise UserDeletedError(msg)
        if isinstance(event, UpdateUserFullNameEvent):
            self.user_full_name = UserFullName(
                user_first_name=UserFirstNameValueObject(event.new_user_first_name),
                user_middle_name=UserMiddleNameValueObject(event.new_user_middle_name),
                user_last_name=UserLastNameValueObject(event.new_user_last_name),
            )
        elif isinstance(event, UpdateUserContactEvent):
            self.user_contact = UserContact(
                user_email=UserEmailValueObject(event.new_user_email),
                user_phone=UserPhoneValueObject(event.new_user_phone),
            )

    @staticmethod
    def replay_events(events: list[BaseDomainEvent]) -> "UserDomainEntity":
        if not isinstance(events[0], CreateUserEvent):
            msg = "First event must be CreateUserEvent"
            raise EventsConsistencyError(msg)
        user: UserDomainEntity = UserDomainEntity(
            uuid=UUIDValueObject(event.uuid),
            user_contact=UserContact(
                user_email=UserEmailValueObject(event.user_email),
                user_phone=UserPhoneValueObject(event.user_phone),
            ),
            user_full_name=UserFullName(
                user_first_name=UserFirstNameValueObject(event.user_first_name),
                user_middle_name=UserMiddleNameValueObject(event.user_middle_name),
                user_last_name=UserLastNameValueObject(event.user_last_name),
            ),
        )
        for event in events[1:]:
            user._apply(event)
        return user
