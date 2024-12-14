from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class AddAddressCommand:
    profile_id: UUID
    profile_owner_id: UUID
    city: str
    country: str
    street: str
    house_number: str
    apartment_number: str
    postal_code: str
