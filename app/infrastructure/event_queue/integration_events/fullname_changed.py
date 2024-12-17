from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.fullname_changed import FullnameChanged as DomainEventFullnameChanged
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class FullnameChanged(IntegrationEvent):
    profile_owner_id: UUID
    profile_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None


def fullname_changed_to_integration(
    event: DomainEventFullnameChanged,
) -> FullnameChanged:
    return FullnameChanged(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_owner_id=event.profile_owner_id,
        profile_id=event.profile_id,
        first_name=event.first_name,
        last_name=event.last_name,
        middle_name=event.middle_name,
    )
