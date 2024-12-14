from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DeleteSocialNetwProfileCommand:
    profile_id: UUID
    profile_owner_id: UUID
    social_netw_profile_id: UUID
