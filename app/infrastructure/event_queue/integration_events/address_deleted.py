from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.address_deleted import AddressDeleted as DomainEventAddressDeleted
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class AddressDeleted(IntegrationEvent):
    profile_id: UUID
    profile_owner_id: UUID
    address_id: UUID


def address_deleted_to_integration(
    event: DomainEventAddressDeleted,
) -> AddressDeleted:
    return AddressDeleted(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_id=event.profile_id,
        profile_owner_id=event.profile_owner_id,
        address_id=event.address_id,
    )
