from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ChangeFullnameCommand:
    profile_id: UUID
    profile_owner_id: UUID
    first_name: str
    middle_name: str | None
    last_name: str
