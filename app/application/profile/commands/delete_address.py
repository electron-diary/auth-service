from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DeleteAddressCommand:
    profile_id: UUID
    profile_owner_id: UUID
    address_id: UUID
