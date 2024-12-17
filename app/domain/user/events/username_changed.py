from dataclasses import dataclass
from uuid import UUID

from app.domain.common.domain_event import DomainEvent


@dataclass(frozen=True)
class UsernameChanged(DomainEvent):
    user_id: UUID
    username: str
