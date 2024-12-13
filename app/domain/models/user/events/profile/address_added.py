from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent


@dataclass(frozen=True)
class AddressAdded(DomainEvent):
    profile_id: UUID
    profile_owner_id: UUID
    address_id: UUID
    city: str
    country: str
    street: str
    house_number: str
    apartment_number: str
    postal_code: str
