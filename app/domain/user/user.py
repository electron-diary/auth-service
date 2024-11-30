from dataclasses import dataclass
from typing import Self

from app.domain.base.agregate_root import AgregateRoot
from app.domain.base.domain_entity import DomainEntity
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored
from app.domain.user.exceptions import UserException
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


@dataclass
class User(DomainEntity[UserId], AgregateRoot):
    username: Username
    contacts: Contacts
    is_deleted: DeletedUser

    @classmethod
    def create_user(
        cls, id: UserId, username: Username, contacts: Contacts, is_deleted: DeletedUser,
    ) -> "User":
        user: User = cls(
            id=id, username=username, contacts=contacts, is_deleted=is_deleted.value,
        )
        action: UserCreated = UserCreated(
            user_id=id.value, username=username.value,
            phone_number=contacts.phone, is_deleted=is_deleted.value,
            event_name="UserCreated", agregate_id=id.value, agregate_name="User",
        )
        user._add_event(event=action)
        return user

    def update_username(self: Self, username: Username) -> None:
        if self.is_deleted.value:
            raise UserException("User is deleted")
        action: UsernameUpdated = UsernameUpdated(
            user_id=self.id.value, username=username.value,
            event_name="UsernameUpdated", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def update_contact(self: Self, contacts: Contacts) -> None:
        if self.is_deleted.value:
            raise UserException("User is deleted")
        action: ContactsUpdated = ContactsUpdated(
            user_id=self.id.value, phone_number=contacts.phone,
            event_name="ContactsUpdated", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def delete_user(self: Self) -> None:
        if self.is_deleted.value:
            raise UserException("User is already deleted")
        action: UserDeleted = UserDeleted(
            user_id=self.id.value, is_deleted=True,
            event_name="UserDeleted", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def recovery_user(self: Self) -> None:
        if not self.is_deleted.value:
            raise UserException("User is not deleted")
        action: UserRestored = UserRestored(
            user_id=self.id.value, is_deleted=False,
            event_name="UserRestored", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def _apply(self: Self, action: DomainEvent) -> None:
        match action:
            case UsernameUpdated():
                self.username = Username(action.username)
            case ContactsUpdated():
                self.contacts = Contacts(phone=action.phone_number)
            case UserDeleted():
                self.is_deleted = DeletedUser(action.is_deleted)
            case UserRestored():
                self.is_deleted = DeletedUser(action.is_deleted)
            case _:
                pass
