from dataclasses import dataclass, field
from typing import Self

from app.domain.base.domain_entity import DomainEntity
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored
from app.domain.user.exceptions import UserException
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


@dataclass
class User(DomainEntity[UserId]):
    """
    User domain entity representing a user in the system.
    Implements event sourcing pattern to track all changes to user state.
    Inherits from DomainEntity with UserId as the identifier type.
    """

    # Internal list to store domain events before they are committed
    _events: list[DomainEvent] = field(default_factory=list, init=False)
    # Value object for user's username
    username: Username
    # Value object containing user's contact information
    contacts: Contacts  
    # Value object tracking user's deletion status
    is_deleted: DeletedUser

    @classmethod
    def create_user(
        cls, id: UserId, username: Username, contacts: Contacts, is_deleted: DeletedUser,
    ) -> "User":
        """
        Factory method to create a new User instance.
        Records a UserCreated event.

        Args:
            id: Unique identifier for the user
            username: User's username value object
            contacts: User's contact information
            is_deleted: Initial deletion status

        Returns:
            A new User instance
        """
        user: User = cls(
            id=id, username=username, contacts=contacts, is_deleted=is_deleted,
        )
        action: UserCreated = UserCreated(
            user_id=id.value, username=username.value,
            phone_number=contacts.phone, is_deleted=is_deleted.value,
            event_name="UserCreated", agregate_id=id.value, agregate_name="User",
        )
        user._add_event(event=action)
        return user

    def update_username(self: Self, username: Username) -> None:
        """
        Updates the user's username if the user is not deleted.
        Records a UsernameUpdated event.

        Args:
            username: New username value object

        Raises:
            UserException: If user is marked as deleted
        """
        if self.is_deleted.value:
            raise UserException("User is deleted")
        action: UsernameUpdated = UsernameUpdated(
            user_id=self.id.value, username=username.value,
            event_name="UsernameUpdated", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def update_contact(self: Self, contacts: Contacts) -> None:
        """
        Updates user's contact information if user is not deleted.
        Records a ContactsUpdated event.

        Args:
            contacts: New contact information value object

        Raises:
            UserException: If user is marked as deleted
        """
        if self.is_deleted.value:
            raise UserException("User is deleted")
        action: ContactsUpdated = ContactsUpdated(
            user_id=self.id.value, phone_number=contacts.phone,
            event_name="ContactsUpdated", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def delete_user(self: Self) -> None:
        """
        Marks the user as deleted.
        Records a UserDeleted event.

        Raises:
            UserException: If user is already marked as deleted
        """
        if self.is_deleted.value:
            raise UserException("User is already deleted")
        action: UserDeleted = UserDeleted(
            user_id=self.id.value, is_deleted=True,
            event_name="UserDeleted", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def recovery_user(self: Self) -> None:
        """
        Restores a previously deleted user.
        Records a UserRestored event.

        Raises:
            UserException: If user is not currently deleted
        """
        if not self.is_deleted.value:
            raise UserException("User is not deleted")
        action: UserRestored = UserRestored(
            user_id=self.id.value, is_deleted=False,
            event_name="UserRestored", agregate_id=self.id.value, agregate_name="User",
        )
        self._apply(action=action)
        self._add_event(event=action)

    def _apply(self: Self, action: DomainEvent) -> None:
        """
        Applies domain events to update the user's state.
        Uses pattern matching to handle different event types.

        Args:
            action: Domain event to apply to user state
        """
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
    
    def _add_event(self: Self, event: DomainEvent) -> None:
        """
        Adds a domain event to the pending events list.

        Args:
            event: Domain event to be recorded
        """
        self._events.append(event)

    def get_events(self: Self) -> list[DomainEvent]:
        """
        Retrieves and clears all pending domain events.

        Returns:
            List of pending domain events
        """
        actions: list[DomainEvent] = self._events.copy()
        self._events.clear()
        return actions
