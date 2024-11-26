from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Self

from app.domain.base.domain_entity import DomainEntity
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserDeleted, UsernameUpdated, UserRestored
from app.domain.user.exceptions import UserException
from app.domain.user.value_objects import Contacts, CreatedDate, DeleteDate, UserId, Username


@dataclass
class User(DomainEntity):
    _actions: list[DomainEvent] = field(default_factory=list, init=False)
    id: UserId
    username: Username
    contacts: Contacts
    created_at: CreatedDate
    delete_date: DeleteDate

    def update_username(self: Self, username: Username) -> None:
        if self.delete_date.value is not None:
            raise UserException("User is deleted")
        if self.created_at.value - datetime.now() < timedelta(days=3):
            raise UserException("User is not old enough to update username")
        action: UsernameUpdated = UsernameUpdated(user_id=self.id.value, username=username.value)
        self._apply(action=action)
        self._add_action(action=action)

    def update_contacts(self: Self, contacts: Contacts) -> None:
        if self.delete_date.value is None:
            raise UserException("User is not deleted")
        if contacts.email is None and contacts.phone is None:
            raise UserException("At least one contact (email or phone) must be provided.")
        if self.created_at.value - datetime.now() < timedelta(days=3):
            raise UserException("User is not old enough to update contacts")
        action: ContactsUpdated = ContactsUpdated(
            user_id=self.id.value, email=contacts.email, phone_number=contacts.phone,
        )
        self._apply(action=action)
        self._add_action(action=action)

    def delete_user(self: Self) -> None:
        if self.delete_date.value is not None:
            raise UserException("User is already deleted")
        if self.created_at.value - datetime.now() < timedelta(days=3):
            raise UserException("User is not old enough to delete")
        action: UserDeleted = UserDeleted(user_id=self.id.value, deleted_date=datetime.now())
        self._apply(action=action)
        self._add_action(action=action)

    def recovery_user(self: Self) -> None:
        if self.delete_date.value is None:
            raise UserException("User is not deleted")
        if self.delete_date.value - datetime.now() > timedelta(days=3):
            raise UserException("Cant't recovery after 30 days")
        action: UserRestored = UserRestored(user_id=self.id.value, deleted_date=None)
        self._apply(action=action)
        self._add_action(action=action)

    def _apply(self: Self, action: DomainEvent) -> None:
        if isinstance(action, UsernameUpdated):
            self.username.value = action.username
        if isinstance(action, ContactsUpdated):
            self.contacts.email = action.email
            self.contacts.phone = action.phone_number
        if isinstance(action, UserDeleted):
            self.delete_date.value = action.deleted_date
        if isinstance(action, UserRestored):
            self.delete_date.value = action.deleted_date

    def _add_action(self: Self, action: DomainEvent) -> None:
        self._actions.append(action)

    def get_actions(self: Self) -> list[DomainEvent]:
        actions: list[DomainEvent] = self._actions.copy()
        self._actions.clear()
        return actions