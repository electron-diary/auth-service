from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent



@dataclass(frozen=True)
class ProfilePicturesChanged(DomainEvent):
    user_id: UUID
    profile_pictures: list[str]