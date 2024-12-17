from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.profile_deleted import ProfileDeleted as DomainEventProfileDeleted
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class ProfileDeleted(IntegrationEvent):
    profile_owner_id: UUID
    profile_id: UUID


def profile_deleted_to_integration(
    event: DomainEventProfileDeleted,
) -> ProfileDeleted:
    return ProfileDeleted(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_owner_id=event.profile_owner_id,
        profile_id=event.profile_id,
    )
