from dataclasses import dataclass
from uuid import UUID
from typing import Optional
from datetime import datetime

from app.application.base.base_dto import BaseDto


@dataclass(frozen=True)
class UserDto(BaseDto):
    user_uuid: UUID
    user_first_name: str
    user_last_name: str
    user_middle_name: Optional[str]
    user_email: Optional[str]
    user_phone: Optional[str]
    user_created_at: datetime
    user_updated_at: datetime

