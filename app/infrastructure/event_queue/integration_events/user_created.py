from dataclasses import dataclass
from uuid import UUID

from app.domain.user.events.user_created import UserCreated as DomainEventUserCreated
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class UserCreated(IntegrationEvent):
    user_id: UUID
    email: str
    phone_number: int
    status: str
    username: str


def user_created_to_integration(
    event: DomainEventUserCreated,
) -> UserCreated:
    return UserCreated(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        user_id=event.user_id,
        email=event.email,
        phone_number=event.phone,
        status=event.status,
        username=event.username,
    )
