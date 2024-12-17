from dataclasses import dataclass
from uuid import UUID

from app.domain.user.events.contacts_changed import ContactsChanged as DomainEventContactsChanged
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class ContactsChanged(IntegrationEvent):
    user_id: UUID
    email: str
    phone_number: int


def contacts_changed_to_integration(
    event: DomainEventContactsChanged,
) -> ContactsChanged:
    return ContactsChanged(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        user_id=event.user_id,
        email=event.email,
        phone_number=event.phone,
    )
