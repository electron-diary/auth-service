from dataclasses import dataclass
from uuid import UUID

from app.domain.base.domain_event import DomainEvent


@dataclass(frozen=True)
class UserCreated(DomainEvent):
    """
    Event emitted when a new user is created in the system.
    
    Attributes:
        user_id (UUID): Unique identifier for the user
        username (str): User's chosen display name
        phone_number (int): User's contact number
        is_deleted (bool): Flag indicating if the user account is marked as deleted
    """

    user_id: UUID
    username: str
    phone_number: int
    is_deleted: bool


@dataclass(frozen=True)
class ContactsUpdated(DomainEvent):
    """
    Event emitted when a user updates their contact information.
    
    Attributes:
        user_id (UUID): Unique identifier for the user
        phone_number (int): Updated phone number
    """

    user_id: UUID
    phone_number: int


@dataclass(frozen=True)
class UsernameUpdated(DomainEvent):
    """
    Event emitted when a user changes their username.
    
    Attributes:
        user_id (UUID): Unique identifier for the user
        username (str): New username chosen by the user
    """

    user_id: UUID
    username: str


@dataclass(frozen=True)
class UserDeleted(DomainEvent):
    """
    Event emitted when a user account is marked as deleted.
    
    Attributes:
        user_id (UUID): Unique identifier for the user
        is_deleted (bool): Flag indicating the deleted status (should be True)
    """

    user_id: UUID
    is_deleted: bool


@dataclass(frozen=True)
class UserRestored(DomainEvent):
    """
    Event emitted when a previously deleted user account is restored.
    
    Attributes:
        user_id (UUID): Unique identifier for the user
        is_deleted (bool): Flag indicating the deleted status (should be False)
    """

    user_id: UUID
    is_deleted: bool
