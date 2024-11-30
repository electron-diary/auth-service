from dataclasses import dataclass
from uuid import UUID

from app.domain.base.domain_event import DomainEvent


@dataclass(frozen=True)
class UserCreated(DomainEvent):
    user_id: UUID
    username: str
    phone_number: int 
    is_deleted: bool

@dataclass(frozen=True)
class ContactsUpdated(DomainEvent):
    user_id: UUID
    phone_number: int 

@dataclass(frozen=True)
class UsernameUpdated(DomainEvent):
    user_id: UUID
    username: str

@dataclass(frozen=True)
class UserDeleted(DomainEvent):
    user_id: UUID
    is_deleted: bool

@dataclass(frozen=True)
class UserRestored(DomainEvent):
    user_id: UUID
    is_deleted: bool
