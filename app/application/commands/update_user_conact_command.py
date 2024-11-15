from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class UpdateUserContactCommand(BaseCommand):
    user_uuid: UUID
    new_user_email: str | None
    new_user_phone: str | None
