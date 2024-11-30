from dataclasses import dataclass, field
from uuid import uuid4, UUID
from datetime import datetime


@dataclass(frozen=True)
class IntegrationEvent:
    event_uuid: UUID = field(default_factory=uuid4, init=False)
    event_date: datetime = field(default_factory=datetime.now, init=False)
    event_name: str

@dataclass(frozen=True)
class UserCreatedIntegrationEvent(IntegrationEvent):
    user_id: UUID
    username: str
    phone_number: int
    is_deleted: bool

@dataclass(frozen=True)
class ContactsUpdatedIntegrationEvent(IntegrationEvent):
    user_id: UUID
    phone_number: int

@dataclass(frozen=True)
class UsernameUpdatedIntegrationEvent(IntegrationEvent):
    user_id: UUID
    username: str

@dataclass(frozen=True)
class UserDeletedIntegrationEvent(IntegrationEvent):
    user_id: UUID
    is_deleted: bool

@dataclass(frozen=True)
class UserRestoredIntegrationEvent(IntegrationEvent):
    user_id: UUID
    is_deleted: bool