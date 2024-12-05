from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent


@dataclass(frozen=True)
class ContactsChanged(DomainEvent):
    user_id: UUID
    phone_number: int | None
    email: str | None