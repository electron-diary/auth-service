from dataclasses import dataclass
from uuid import UUID
from typing import Optional

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    user_uuid: UUID
    user_email: Optional[str] = None
    user_phone: Optional[int] = None
    user_middle_name: Optional[str] = None
    user_first_name: str
    user_last_name: str
    