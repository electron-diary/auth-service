from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from app.domain.common.event import DomainEvent


@dataclass(frozen=True)
class CreateUserEvent(DomainEvent):
    user_uuid: UUID
    user_name: str
    user_contact: str
    user_created_at: datetime
    user_updated_at: datetime
