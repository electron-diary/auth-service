from typing import Self
from uuid import UUID

from app.domain.agregate_root import AgregateRoot
from app.domain.profile.entities.address import Address
from app.domain.profile.entities.social_netw_profile import SocialNetwProfile
from app.domain.profile.enums.statuses import Statuses
from app.domain.profile.events.address_added import AddressAdded
from app.domain.profile.events.address_deleted import AddressDeleted
from app.domain.profile.events.bio_changed import BioChanged
from app.domain.profile.events.fullname_changed import FullnameChanged
from app.domain.profile.events.profile_created import ProfileCreated
from app.domain.profile.events.profile_deleted import ProfileDeleted
from app.domain.profile.events.profile_status_changed import ProfileStatusChanged
from app.domain.profile.events.social_netw_profile_added import SocialNetwProfileAdded
from app.domain.profile.events.social_netw_profile_deleted import SocialNetwProfileDeleted
from app.domain.profile.exceptions import (
    AddressNotFoundError,
    ProfileInactiveError,
    SocialNetwProfileNotFoundError,
)
from app.domain.profile.value_objects.fullname import Fullname
from app.domain.unit_of_work import UnitOfWorkTracker
from app.domain.uowed import UowedEntity


class Profile(UowedEntity[UUID], AgregateRoot):
    def __init__(
        self: Self,
        uow: UnitOfWorkTracker,
        profile_id: UUID,
        profile_owner_id: UUID,
        fullname: Fullname,
        profile_status: Statuses,
        bio: str,
        addresses: list[Address] = [],
        social_netw_profiles: list[SocialNetwProfile] = [],
    ) -> None:
        super().__init__(uow=uow, id=profile_id)

        self.profile_owner_id = profile_owner_id
        self.fullname = fullname
        self.status = profile_status
        self.bio = bio
        self.addresses = addresses
        self.social_netw_profiles = social_netw_profiles

    @classmethod
    def create_profile(
        cls: type[Self],
        uow: UnitOfWorkTracker,
        profile_id: UUID,
        profile_owner_id: UUID,
        first_name: str,
        last_name: str,
        middle_name: str | None,
        bio: str,
    ) -> Self:
        profile = cls(
            uow=uow,
            profile_id=profile_id,
            profile_owner_id=profile_owner_id,
            fullname=Fullname(
                first_name=first_name, last_name=last_name, middle_name=middle_name,
            ),
            profile_status=Statuses.ACTIVE,
            bio=bio,
        )
        profile.mark_new()
        profile.record_event(
            ProfileCreated(
                aggregate_id=profile.profile_id,
                event_type="ProfileCreated",
                agregate_name="Profile",
                profile_status=profile.status.value,
                profile_id=profile.profile_id,
                profile_owner_id=profile.profile_owner_id,
                first_name=profile.fullname.first_name,
                last_name=profile.fullname.last_name,
                middle_name=profile.fullname.middle_name,
                bio=profile.bio,
            ),
        )

        return profile

    def add_address(
        self: Self,
        address_id: UUID,
        city: str,
        country: str,
        street: str,
        house_number: str,
        apartment_number: str,
        postal_code: str,
    ) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        address = Address.create_address(
            uow=self.uow,
            profile_id=self.id,
            address_id=address_id,
            city=city,
            country=country,
            street=street,
            house_number=house_number,
            apartment_number=apartment_number,
            postal_code=postal_code,
        )
        self.addresses.append(address)
        self.record_event(
            AddressAdded(
                aggregate_id=self.id,
                event_type="AddressAdded",
                agregate_name="Profile",
                address_id=address.id,
                city=address.city,
                country=address.country,
                street=address.street,
                house_number=address.house_number,
                apartment_number=address.apartament_number,
                postal_code=address.postal_code,
            ),
        )

    def delete_address(self: Self, address_id: UUID) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        for address in self.addresses:
            if address.id == address_id:
                address.delete_address()
                self.record_event(
                    AddressDeleted(
                        aggregate_id=self.id,
                        event_type="AddressDeleted",
                        agregate_name="Profile",
                        address_id=address.id,
                        profile_id=self.id,
                        profile_owner_id=self.profile_owner_id,
                    ),
                )

        raise AddressNotFoundError("Address not found")

    def add_social_netw_profile(
        self: Self,
        social_netw_profile_id: UUID,
        social_netw_profile_name: str,
        social_netw_profile_url: str,
    ) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        social_netw_profile = SocialNetwProfile.create_social_netw_profile(
            uow=self.uow,
            social_netw_profile_id=social_netw_profile_id,
            social_netw_profile_name=social_netw_profile_name,
            social_netw_profile_url=social_netw_profile_url,
            profile_id=self.id,
        )
        self.social_netw_profiles.append(social_netw_profile)
        self.record_event(
            SocialNetwProfileAdded(
                aggregate_id=self.id,
                event_type="SocialNetwProfileAdded",
                agregate_name="Profile",
                profile_id=self.id,
                profile_owner_id=self.profile_owner_id,
                social_netw_profile_id=social_netw_profile_id,
                social_netw_profile_url=social_netw_profile_url,
                social_netw_profile_type=social_netw_profile_name,
            ),
        )

    def delete_social_netw_profile(self: Self, social_netw_profile_id: UUID) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        for social_netw_profile in self.social_netw_profiles:
            if social_netw_profile.id == social_netw_profile_id:
                social_netw_profile.delete_social_netw_profile()
                self.record_event(
                    SocialNetwProfileDeleted(
                        aggregate_id=self.id,
                        event_type="SocialNetwProfileDeleted",
                        agregate_name="Profile",
                        profile_id=self.id,
                        profile_owner_id=self.profile_owner_id,
                        social_netw_profile_id=social_netw_profile.id,
                    ),
                )

        raise SocialNetwProfileNotFoundError("Social netw profile not found")

    def change_bio(self: Self, bio: str) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        self.bio = bio
        self.mark_dirty()
        self.record_event(
            BioChanged(
                aggregate_id=self.id,
                event_type="BioChanged",
                agregate_name="Profile",
                profile_id=self.id,
                profile_owner_id=self.profile_owner_id,
                bio=bio,
            ),
        )

    def change_fullname(self: Self, first_name: str, last_name: str, middle_name: str| None) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        self.fullname = Fullname(
            first_name=first_name, last_name=last_name, middle_name=middle_name,
        )
        self.mark_dirty()
        self.record_event(
            FullnameChanged(
                aggregate_id=self.id,
                event_type="FullnameChanged",
                agregate_name="Profile",
                profile_id=self.id,
                profile_owner_id=self.profile_owner_id,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
            ),
        )

    def change_status(self: Self, status: Statuses) -> None:
        self.status = status
        self.mark_dirty()
        self.record_event(
            ProfileStatusChanged(
                aggregate_id=self.id,
                event_type="ProfileStatusChanged",
                agregate_name="Profile",
                profile_id=self.id,
                profile_owner_id=self.profile_owner_id,
                status=status.value,
            ),
        )

    def delete_profile(self: Self) -> None:
        self.mark_deleted()

        for address in self.addresses:
            address.delete_address()

        for social_netw_profile in self.social_netw_profiles:
            social_netw_profile.delete_social_netw_profile()

        for avatar in self.avatars:
            avatar.delete_avatar()

        self.record_event(
            ProfileDeleted(
                aggregate_id=self.id,
                event_type="ProfileDeleted",
                agregate_name="Profile",
                profile_id=self.id,
                profile_owner_id=self.profile_owner_id,
            ),
        )
