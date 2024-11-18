from dataclasses import dataclass
from uuid import UUID

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class UpdateUserFullNameEvent(BaseDomainEvent):
    user_uuid: UUID
    new_user_first_name: str | None
    new_user_middle_name: str | None
    new_user_last_name: str | None
