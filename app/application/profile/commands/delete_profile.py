from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DeleteProfileCommand:
    profile_id: UUID
    profile_owner_id: UUID
