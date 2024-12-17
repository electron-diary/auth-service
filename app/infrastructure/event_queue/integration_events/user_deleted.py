from dataclasses import dataclass
from uuid import UUID

from app.domain.user.events.user_deleted import UserDeleted as DomainEventUserDeleted
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class UserDeleted(IntegrationEvent):
    user_id: UUID


def user_deleted_to_integration(
    event: DomainEventUserDeleted,
) -> UserDeleted:
    return UserDeleted(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        user_id=event.user_id,
    )
