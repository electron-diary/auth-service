from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class AddSocialNetwProfileCommand:
    profile_id: UUID
    profile_owner_id: UUID
    social_netw_name: str
    social_netw_url: str
