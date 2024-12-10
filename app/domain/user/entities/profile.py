from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.entities.avatar import Avatar
from app.domain.user.entities.social_network import SocialNetwork
from app.domain.user.entities.address import Address


class Profile(UowedEntity[None]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: ...,
        avatars: list[Avatar],
        social_networks: list[SocialNetwork],
        addresses: list[Address],
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.avatars: list[Avatar] = avatars
        self.social_networks: list[SocialNetwork] = social_networks
        self.addresses: list[Address] = addresses

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        profile = cls(uow=uow, id=None)
        profile.mark_new()

        return profile
    
    def add_address(
        self: Self,
        address_id: UUID,
        city: str,
        region: str,
        street: str,
        house_location: str
    ) -> None:
        address: Address = Address.create(
            uow=self.uow,
            id=address_id,
            city=city,
            region=region,
            street=street,
            house_location=house_location
        )
        self.addresses.append(address)

    def delete_address(self: Self, address_id: UUID) -> None:
        for address in self.addresses:
            if address.id.value == address_id:
                address.delete()

    def edit_city(self: Self, address_id: UUID, city: str) -> None:
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_city(city=city)

    def edit_region(self: Self, address_id: UUID, region: str) -> None:
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_region(region=region)

    def edit_street(self: Self, address_id: UUID, street: str) -> None:
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_street(street=street)

    def edit_house_location(self: Self, address_id: UUID, house_location: str) -> None:
        for address in self.addresses:
            if address.id.value == address_id:
                address.edit_house_location(house_location=house_location)

    def add_avatar(
        self: Self,
        file_id: UUID,
        file_name: str,
        file_size: int,
        file_extension: str,
    ) -> None:
        avatar: Avatar = Avatar.create(
            uow=self.uow,
            file_id=file_id,
            file_name=file_name,
            file_size=file_size,
            file_extension=file_extension
        )
        self.avatars.append(avatar)

    def delete_avatar(self: Self, file_id: UUID):
        for avatar in self.avatars:
            if avatar.id.value == file_id:
                avatar.delete()
                
    def add_social_network(self: Self) -> None:
        social_network: SocialNetwork = SocialNetwork.create(uow=self.uow)
        self.social_networks.append(social_network)

    def delete_social_network(self: Self):
        for social_network in self.social_networks:
            if social_network.id == ...:
                social_network.delete()

    def delete(self: Self) -> None:
        for avatar in self.avatars:
            avatar.delete()

        for social_network in self.social_networks:
            social_network.delete()

        for address in self.addresses:
            address.delete()
        
        self.mark_deleted()
