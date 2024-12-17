from dataclasses import dataclass
from uuid import UUID

from app.domain.common.domain_event import DomainEvent


@dataclass(frozen=True)
class FullnameChanged(DomainEvent):
    profile_owner_id: UUID
    profile_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
