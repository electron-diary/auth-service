from dataclasses import dataclass, field
from uuid import UUID

from app.domain.common.common_domain_event import CommonDomainEvent


@dataclass(frozen=True)
class UserCreatedEvent(CommonDomainEvent):
    id: UUID
    email: str | None = field(default=None)
    phone: str | None = field(default=None)
    username: str

