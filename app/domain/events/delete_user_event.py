from dataclasses import dataclass
from uuid import UUID

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class DeleteUserEvent(BaseDomainEvent):
    user_uuid: UUID
