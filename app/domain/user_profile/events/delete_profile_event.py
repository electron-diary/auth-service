from dataclasses import dataclass
from uuid import UUID

from app.domain.common.common_domain_event import CommonDomainEvent


@dataclass(frozen=True)
class ProfileDeletedEvent(CommonDomainEvent):
    id: UUID
