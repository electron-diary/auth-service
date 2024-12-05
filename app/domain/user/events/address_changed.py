from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent


@dataclass(frozen=True)
class AddressChanged(DomainEvent):
    user_id: UUID
    country: str | None
    city: str | None
    street: str | None
    house_location: str | None