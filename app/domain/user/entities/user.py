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
    
    def add_address(
        self: Self,
        address_id: UUID,
        city: str,
        region: str,
        street: str,
        house_location: str
    ) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.add_address(
                    address_id=address_id,
                    city=city,
                    region=region,
                    street=street,
                    house_location=house_location
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
    
    def add_profile(self: Self) -> None:
        profile = Profile.create(uow=self.uow)
        self.profiles.append(profile)

    def delete_profile(self: Self) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete()

    def add_avatar(self: Self) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.add_avatar()

    def delete_avatar(self: Self) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete_avatar()

    def add_social_network(self: Self) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.add_social_network()

    def delete_social_network(self: Self) -> None:
        for profile in self.profiles:
            if profile.id == ...:
                profile.delete_social_network()

    def delete(self: Self) -> None:
        self.mark_deleted()
        for profile in self.profiles:
            profile.delete()
