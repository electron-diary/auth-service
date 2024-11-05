from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from app.domain.common.event import DomainEvent


@dataclass(frozen=True)
class UpdateUserNameEvent(DomainEvent):
    user_uuid: UUID
    new_user_name: str
    user_updated_at: datetime