from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.entities.profile import Profile


class User(UowedEntity[None]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: ...,
        profiles: list[Profile],
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.profiles: list[Profile] = profiles

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        user = cls(uow=uow, id=None)
        user.mark_new()

        return user

    def add_profile(self: Self) -> None:
        profile = Profile.create(uow=self.uow)
        self.profiles.append(profile)

    def add_address(
        self: Self,
        address_id: UUID,
        city: str,
        region: str,
        street: str,
        house_location: str,
    ) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.add_address(
                    address_id=address_id,
                    city=city,
                    region=region,
                    street=street,
                    house_location=house_location,
                )

    def add_avatar(
        self: Self,
        file_id: UUID,
        file_name: str,
        file_size: int,
        file_extension: str,
    ) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.add_avatar(
                    file_id=file_id,
                    file_name=file_name,
                    file_size=file_size,
                    file_extension=file_extension,
                )

    def add_social_network(
        self: Self,
        social_network_id: UUID,
        social_network_link: str,
        social_network_type: str,
    ) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.add_social_network(
                    social_network_id=social_network_id,
                    social_network_link=social_network_link,
                    social_network_type=social_network_type,
                )

    def edit_city(self: Self, address_id: UUID, city: str) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.edit_city(address_id=address_id, city=city)

    def edit_region(self: Self, address_id: UUID, region: str) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.edit_region(address_id=address_id, region=region)

    def edit_street(self: Self, address_id: UUID, street: str) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.edit_street(address_id=address_id, street=street)

    def edit_house_location(self: Self, address_id: UUID, house_location: str) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.edit_house_location(address_id=address_id, house_location=house_location)

    def delete_address(self: Self, address_id: UUID) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete_address(address_id=address_id)

    def delete_profile(self: Self) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete()

    def delete_avatar(self: Self, file_id: UUID) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete_avatar(file_id=file_id)

    def delete_social_network(self: Self, social_network_id: UUID) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete_social_network(social_network_id=social_network_id)

    def delete(self: Self) -> None:
        self.mark_deleted()
        for profile in self.profiles:
            profile.delete()
