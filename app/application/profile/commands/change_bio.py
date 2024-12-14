from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class ChangeBioCommand:
    profile_id: UUID
    profile_owner_id: UUID
    bio: str
