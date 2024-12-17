from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.bio_changed import BioChanged as DomainEventBioChanged
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class BioChanged(IntegrationEvent):
    profile_owner_id: UUID
    profile_id: UUID
    bio: str


def bio_changed_to_integration(
    event: DomainEventBioChanged,
) -> BioChanged:
    return BioChanged(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_owner_id=event.profile_owner_id,
        profile_id=event.profile_id,
        bio=event.bio,
    )
