from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent


@dataclass(frozen=True)
class AvatarAdded(DomainEvent):
    profile_owner_id: UUID
    profile_id: UUID
    avatar_id: UUID
    file_name: str
    file_url: str
    file_extension: str
    file_size: int
