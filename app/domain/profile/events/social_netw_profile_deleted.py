from dataclasses import dataclass
from uuid import UUID

from app.domain.common.domain_event import DomainEvent


@dataclass(frozen=True)
class SocialNetwProfileDeleted(DomainEvent):
    profile_owner_id: UUID
    profile_id: UUID
    social_netw_profile_id: UUID
