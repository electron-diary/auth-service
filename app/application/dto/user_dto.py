from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from datetime import datetime


@dataclass(frozen=True)
class UserDto:
    user_uuid: UUID
    user_first_name: str
    user_last_name: str
    user_middle_name: Optional[str] = None
    user_email: Optional[str] = None
    user_phone: Optional[str] = None
    user_created_at: datetime
    user_updated_at: datetime

