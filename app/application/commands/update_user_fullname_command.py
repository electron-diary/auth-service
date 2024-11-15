from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class UpdateUserFullNameCommand(BaseCommand):
    user_uuid: UUID
    new_user_first_name: str | None
    new_user_middle_name: str | None
    new_user_last_name: str | None
