from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_dto import BaseDto


@dataclass(frozen=True)
class UserDto(BaseDto):
    user_uuid: UUID
    user_first_name: str
    user_last_name: str
    user_middle_name: str | None
    user_email: str | None
    user_phone: str | None

