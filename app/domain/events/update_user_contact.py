from dataclasses import dataclass
from uuid import UUID

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class UpdateUserContactEvent(BaseDomainEvent):
    uuid: UUID
    new_user_email: str | None
    new_user_phone:int | None
