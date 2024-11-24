from dataclasses import dataclass, field
from datetime import date
from uuid import UUID

from app.domain.common.common_domain_event import CommonDomainEvent


@dataclass(frozen=True)
class ProfileUpdated(CommonDomainEvent):
    id: UUID
    address: str | None = field(default=None)
    birth_date: date | None = field(default=None)
    bio: str | None = field(default=None)
    first_name: str
    last_name: str
    middle_name: str | None = field(default=None)
    gender: str | None = field(default=None)
    interests: list[str] | None = field(default=None)
    profile_picture: list[str] | None = field(default=None)
    profile_type: str
    social_profiles: list[str] | None = field(default=None)
