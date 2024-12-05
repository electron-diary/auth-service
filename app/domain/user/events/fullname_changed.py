from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent


@dataclass(frozen=True)
class FullnameChanged(DomainEvent):
    user_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
