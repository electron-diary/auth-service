from dataclasses import dataclass, field
from uuid import UUID
from datetime import datetime

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class UpdateUserFullNameEvent(BaseDomainEvent):
    uuid: UUID
    new_user_first_name: str | None
    new_user_middle_name: str | None
    new_user_last_name: str | None