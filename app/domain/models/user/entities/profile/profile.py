from typing import Self
from uuid import UUID

from app.domain.agregate_root import AgregateRoot
from app.domain.models.user.entities.profile.address import Address
from app.domain.models.user.entities.profile.avatar import Avatar
from app.domain.models.user.entities.profile.social_netw_profile import SocialNetwProfile
from app.domain.models.user.enums.statuses import Statuses
from app.domain.models.user.exceptions import (
    AddressNotFoundError,
    AvatarNotFoundError,
    ProfileInactiveError,
    SocialNetwProfileNotFoundError,
)
from app.domain.models.user.vos.fullname import Fullname
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class Profile(UowedEntity[UUID], AgregateRoot):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        profile_id: UUID,
        profile_owner_id: UUID,
        fullname: Fullname,
        profile_status: Statuses,
        addresses: list[Address],
        social_netw_profiles: list[SocialNetwProfile],
        avatars: list[Avatar],
        bio: str,
    ) -> None:
        super().__init__(uow=uow, id=profile_id)

        self.profile_owner_id = profile_owner_id
        self.fullname = fullname
        self.status = profile_status
        self.bio = bio
        self.addresses = addresses
        self.social_netw_profiles = social_netw_profiles
        self.avatars = avatars

    @classmethod
    def create_profile(
        cls: type[Self],
        uow: UnitOfWorkInterface,
        profile_id: UUID,
        profile_owner_id: UUID,
        first_name: str,
        last_name: str,
        middle_name: str | None,
        bio: str,
        addresses: list[Address],
        social_netw_profiles: list[SocialNetwProfile],
        avatars: list[Avatar],
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
            addresses=addresses,
            social_netw_profiles=social_netw_profiles,
            avatars=avatars,
        )
        profile.mark_new()

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
            address_id=address_id,
            city=city,
            country=country,
            street=street,
            house_number=house_number,
            apartment_number=apartment_number,
            postal_code=postal_code,
        )
        self.addresses.append(address)

    def change_address(
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

        for address in self.addresses:
            if address.id == address_id:
                address.change_address(
                    city=city,
                    country=country,
                    street=street,
                    house_number=house_number,
                    apartment_number=apartment_number,
                    postal_code=postal_code,
                )

        raise AddressNotFoundError("Address not found")

    def delete_address(self: Self, address_id: UUID) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        for address in self.addresses:
            if address.id == address_id:
                address.delete_address()

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
        )
        self.social_netw_profiles.append(social_netw_profile)

    def delete_social_netw_profile(self: Self, social_netw_profile_id: UUID) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        for social_netw_profile in self.social_netw_profiles:
            if social_netw_profile.id == social_netw_profile_id:
                social_netw_profile.delete_social_netw_profile()

        raise SocialNetwProfileNotFoundError("Social netw profile not found")

    def add_avatar(
        self: Self,
        avatar_id: UUID,
        avatar_url: str,
        file_name: str,
        file_extension: str,
        file_size: int,
    ) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        avatar = Avatar.create_avatar(
            uow=self.uow,
            avatar_id=avatar_id,
            url=avatar_url,
            file_name=file_name,
            file_extension=file_extension,
            file_size=file_size,
        )
        self.avatars.append(avatar)

    def delete_avatar(self: Self, avatar_id: UUID) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        for avatar in self.avatars:
            if avatar.id == avatar_id:
                avatar.delete_avatar()

        raise AvatarNotFoundError("Avatar not found")

    def change_bio(self: Self, bio: str) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        self.bio = bio
        self.mark_dirty()

    def change_fullname(self: Self, first_name: str, last_name: str, middle_name: str| None) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        self.fullname = Fullname(
            first_name=first_name, last_name=last_name, middle_name=middle_name,
        )
        self.mark_dirty()

    def change_status(self: Self, status: Statuses) -> None:
        self.status = status
        self.mark_dirty()

    def delete_profile(self: Self) -> None:
        if self.status == Statuses.INACTIVE:
            raise ProfileInactiveError( "Profile is inactive")

        self.mark_deleted()

        for address in self.addresses:
            address.delete_address()

        for social_netw_profile in self.social_netw_profiles:
            social_netw_profile.delete_social_netw_profile()

        for avatar in self.avatars:
            avatar.delete_avatar()
