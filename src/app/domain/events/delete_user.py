from dataclasses import dataclass
from uuid import UUID
from app.domain.common.event import DomainEvent


@dataclass(frozen=True)
class DeleteUserEvent(DomainEvent):
    user_uuid: UUID