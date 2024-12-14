from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class GetUserProfilesQuery:
    profile_owner_id: UUID
