from dataclasses import dataclass
from uuid import UUID

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class CreateUserEvent(BaseDomainEvent):
    uuid: UUID
    user_email: str | None
    user_phone: int | None
    user_first_name: str
    user_last_name: str
    user_middle_name: str | None
