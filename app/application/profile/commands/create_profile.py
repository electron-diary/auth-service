from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class CreateProfileCommand:
    profile_owner_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    bio: str
