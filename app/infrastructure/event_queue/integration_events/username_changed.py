from dataclasses import dataclass
from uuid import UUID

from app.domain.user.events.username_changed import UsernameChanged as DomainEventUsernameChanged
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class UsernameChanged(IntegrationEvent):
    user_id: UUID
    username: str


def username_changed_to_integration(
    event: DomainEventUsernameChanged,
) -> UsernameChanged:
    return UsernameChanged(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        user_id=event.user_id,
        username=event.username,
    )
