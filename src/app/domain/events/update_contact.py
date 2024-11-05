from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from app.domain.common.event import DomainEvent


@dataclass(frozen=True)
class UpdateUserContactEvent(DomainEvent):
    user_uuid: UUID
    new_user_contact: str
    user_updated_at: datetime