from dataclasses import dataclass
from uuid import UUID
from typing import Optional

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    user_uuid: UUID
    user_email: Optional[str]
    user_phone: Optional[int]
    user_middle_name: Optional[str]
    user_first_name: str
    user_last_name: str
    