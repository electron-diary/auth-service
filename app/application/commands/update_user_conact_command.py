from dataclasses import dataclass
from uuid import UUID
from typing import Optional

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class UpdateUserContactCommand(BaseCommand):
    user_uuid: UUID
    new_user_email: Optional[str]
    new_user_phone: Optional[str]