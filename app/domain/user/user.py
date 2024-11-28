from dataclasses import dataclass, field
from typing import Self

from app.domain.base.domain_entity import DomainEntity
from app.domain.base.domain_event import DomainEvent
from app.domain.base.agregate_root import AgregateRoot
from app.domain.user.actions import ContactsUpdated, UserDeleted, UsernameUpdated, UserRestored
from app.domain.user.exceptions import UserException
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


@dataclass
class User(DomainEntity[UserId], AgregateRoot):
    username: Username
    contacts: Contacts
    is_deleted: DeletedUser

    def update_username(self: Self, username: Username) -> None:
        if self.is_deleted.value:
            raise UserException("User is deleted")
        action: UsernameUpdated = UsernameUpdated(
            user_id=self.id.value, username=username.value, 
            event_name='UsernameUpdated', agregate_id=self.id.value, agregate_name='User'
        )
        self._apply(action=action)
        self._add_event(event=action)

    def update_contacts(self: Self, contacts: Contacts) -> None:
        if self.is_deleted.value:
            raise UserException("User is deleted")
        if contacts.email is None and contacts.phone is None:
            raise UserException("At least one contact (email or phone) must be provided.")
        action: ContactsUpdated = ContactsUpdated(
            user_id=self.id.value, email=contacts.email, phone_number=contacts.phone,
            event_name='ContactsUpdated', agregate_id=self.id.value, agregate_name='User'
        )
        self._apply(action=action)
        self._add_event(event=action)

    def delete_user(self: Self) -> None:
        if self.is_deleted.value:
            raise UserException("User is already deleted")
        action: UserDeleted = UserDeleted(
            user_id=self.id.value, is_deleted=True,
            event_name='UserDeleted', agregate_id=self.id.value, agregate_name='User'
        )
        self._apply(action=action)
        self._add_event(event=action)

    def recovery_user(self: Self) -> None:
        if not self.is_deleted.value:
            raise UserException("User is not deleted")
        action: UserRestored = UserRestored(
            user_id=self.id.value, is_deleted=False, 
            event_name='UserRestored', agregate_id=self.id.value, agregate_name='User'
        )
        self._apply(action=action)
        self._add_event(event=action)

    def _apply(self: Self, action: DomainEvent) -> None:
        match action:
            case UsernameUpdated():
                self.username = Username(action.username)
            case ContactsUpdated():
                self.contacts = Contacts(email=action.email, phone=action.phone_number)
            case UserDeleted():
                self.is_deleted = DeletedUser(action.is_deleted)
            case UserRestored():
                self.is_deleted = DeletedUser(action.is_deleted)
            case _:
                pass
