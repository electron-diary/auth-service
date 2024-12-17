from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.profile_created import ProfileCreated as DomainEventProfileCreated
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class ProfileCreated(IntegrationEvent):
    profile_id: UUID
    profile_owner_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    profile_status: str
    bio: str


def profile_created_to_integration(
    event: DomainEventProfileCreated,
) -> ProfileCreated:
    return ProfileCreated(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_id=event.profile_id,
        profile_owner_id=event.profile_owner_id,
        first_name=event.first_name,
        last_name=event.last_name,
        middle_name=event.middle_name,
        profile_status=event.profile_status,
        bio=event.bio,
    )
