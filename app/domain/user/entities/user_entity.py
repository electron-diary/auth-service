from dataclasses import dataclass, field
from typing import Self

from app.domain.common.agregate_root import AgregateRoot
from app.domain.common.common_domain_entity import CommonDomainEntity
from app.domain.user.events.create_user_event import UserCreatedEvent
from app.domain.user.events.delete_user_event import UserDeletedEvent
from app.domain.user.events.update_user_event import UserUpdatedEvent
from app.domain.user.value_objects.user_contacts_value_object import UserContactsValueObject
from app.domain.user.value_objects.user_uuid_value_object import UserUUID
from app.domain.user.value_objects.username_value_object import UserNameValueObject
from app.domain.user_profile.entities.profile_entity import ProfileEntity


@dataclass
class UserEntity(CommonDomainEntity[UserUUID], AgregateRoot):
    id: UserUUID
    username: UserNameValueObject
    contacts: UserContactsValueObject
    profiles: list[ProfileEntity] = field(default_factory=list)

    @staticmethod
    def create_user(
        id: UserUUID, contacts: UserContactsValueObject, username: UserNameValueObject,
    ) -> "UserEntity":
        event: UserCreatedEvent = UserCreatedEvent(
            id = id, email=contacts.email, phone=contacts.phone, username=username.username,
        )

    def delete_user(self: Self) -> None:
        event: UserDeletedEvent = UserDeletedEvent(self.id)

    def update_user(
        self: Self, contacts: UserContactsValueObject, username: UserNameValueObject,
    ) -> None:
        event: UserUpdatedEvent = UserUpdatedEvent(
            id = self.id, email=contacts.email, phone=contacts.phone, username=username.username,
        )
