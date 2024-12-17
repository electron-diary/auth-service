from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.address_added import AddressAdded as DomainEventAddressAdded
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class AddressAdded(IntegrationEvent):
    profile_id: UUID
    profile_owner_id: UUID
    address_id: UUID
    city: str
    country: str
    street: str
    house_number: str
    apartment_number: str
    postal_code: str


def address_added_to_integration(
    event: DomainEventAddressAdded,
) -> AddressAdded:
    return AddressAdded(
        event_id=event.event_uuid,
        occurred_at=event.occurred_at,
        event_type=event.event_type,
        profile_id=event.profile_id,
        profile_owner_id=event.profile_owner_id,
        address_id=event.address_id,
        city=event.city,
        country=event.country,
        street=event.street,
        house_number=event.house_number,
        apartment_number=event.apartment_number,
        postal_code=event.postal_code,
    )
