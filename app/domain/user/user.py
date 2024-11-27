from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Self

from app.domain.base.domain_entity import DomainEntity
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserDeleted, UsernameUpdated, UserRestored
from app.domain.user.exceptions import UserException
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


@dataclass
class User(DomainEntity):
    _actions: list[DomainEvent] = field(default_factory=list, init=False)
    id: UserId
    username: Username
    contacts: Contacts
    is_deleted: DeletedUser

    def update_username(self: Self, username: Username) -> None:
        if self.is_deleted == True:
            raise UserException("User is deleted")
        action: UsernameUpdated = UsernameUpdated(user_id=self.id.value, username=username.value)
        self._apply(action=action)
        self._add_action(action=action)

    def update_contacts(self: Self, contacts: Contacts) -> None:
        if self.is_deleted.value == True:
            raise UserException("User is deleted")
        if contacts.email is None and contacts.phone is None:
            raise UserException("At least one contact (email or phone) must be provided.")
        action: ContactsUpdated = ContactsUpdated(
            user_id=self.id.value, email=contacts.email, phone_number=contacts.phone,
        )
        self._apply(action=action)
        self._add_action(action=action)

    def delete_user(self: Self) -> None:
        if self.is_deleted.value == True:
            raise UserException("User is already deleted")
        action: UserDeleted = UserDeleted(user_id=self.id.value, is_deleted=True)
        self._apply(action=action)
        self._add_action(action=action)

    def recovery_user(self: Self) -> None:
        if self.is_deleted.value == False:
            raise UserException("User is not deleted")
        action: UserRestored = UserRestored(user_id=self.id.value, is_deleted=False)
        self._apply(action=action)
        self._add_action(action=action)

    def _apply(self: Self, action: DomainEvent) -> None:
        if isinstance(action, UsernameUpdated):
            self.username = Username(action.username)
        if isinstance(action, ContactsUpdated):
            self.contacts = Contacts(email=action.email, phone=action.phone_number)
        if isinstance(action, UserDeleted):
            self.is_deleted = DeletedUser(action.is_deleted)
        if isinstance(action, UserRestored):
            self.is_deleted = DeletedUser(action.is_deleted)

    def _add_action(self: Self, action: DomainEvent) -> None:
        self._actions.append(action)

    def get_actions(self: Self) -> list[DomainEvent]:
        actions: list[DomainEvent] = self._actions.copy()
        self._actions.clear()
        return actions
