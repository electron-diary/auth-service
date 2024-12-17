from dataclasses import dataclass
from uuid import UUID

from app.domain.common.domain_event import DomainEvent


@dataclass(frozen=True)
class AddressDeleted(DomainEvent):
    profile_id: UUID
    profile_owner_id: UUID
    address_id: UUID
