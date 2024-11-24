from dataclasses import dataclass
from uuid import UUID

from app.domain.common.common_domain_event import CommonDomainEvent


@dataclass(frozen=True)
class UserDeleted(CommonDomainEvent):
    id: UUID
