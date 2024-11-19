from dataclasses import dataclass, field
from datetime import datetime

from app.domain.base.base_event import BaseDomainEvent


@dataclass(frozen=True)
class CreateUserEvent(BaseDomainEvent):
    user_email: str | None
    user_phone: int | None
    user_first_name: str
    user_last_name: str
    user_middle_name: str | None
