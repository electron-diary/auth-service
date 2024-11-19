from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class DeleteUserEvent(BaseDomainEvent):
    uuid: UUID
