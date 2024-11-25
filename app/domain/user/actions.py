from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from app.domain.base.domain_event import DomainEvent


@dataclass(frozen=True)
class UserCreated(DomainEvent):
    user_id: UUID
    username: str
    phone_number: int | None
    email: str | None
    created_at: datetime
    deleted_date: datetime | None

@dataclass(frozen=True)
class ContactsUpdated(DomainEvent):
    user_id: UUID
    phone_number: int | None
    email: str | None

@dataclass(frozen=True)
class UsernameUpdated(DomainEvent):
    user_id: UUID
    username: str

@dataclass(frozen=True)
class UserDeleted(DomainEvent):
    user_id: UUID
    deleted_date: datetime

@dataclass(frozen=True)
class UserRestored(DomainEvent):
    user_id: UUID
    deleted_date: None
