from dataclasses import dataclass
from uuid import UUID
from datetime import datetime

from app.domain.common.event import DomainEvent


@dataclass(frozen=True)
class UpdateUserPasswordEvent(DomainEvent):
    user_uuid: UUID
    new_user_password: str
    user_updated_at: datetime