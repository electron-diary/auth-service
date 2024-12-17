from dataclasses import dataclass
from uuid import UUID

from app.domain.common.domain_event import DomainEvent


@dataclass(frozen=True)
class ContactsChanged(DomainEvent):
    user_id: UUID
    email: str | None
    phone: int | None
