from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class AddressData:
    address_id: UUID
    city: str
    country: str
    street: str
    house_number: str
    apartment_number: str
    postal_code: str


@dataclass(frozen=True)
class SocialNetwProfileData:
    social_netw_profile_id: UUID
    social_netw_profile_name: str
    social_netw_profile_link: str


@dataclass(frozen=True)
class ProfileDto:
    profile_id: UUID
    profile_owner_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    status: str
    bio: str
    address: list[AddressData]
    social_netw_profiles: list[SocialNetwProfileData]
