from typing import Self

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
    
    def add_address(self: Self) -> None:
        address: Address = Address.create(uow=self.uow)
        self.addresses.append(address)

    def delete_address(self: Self):
        for address in self.addresses:
            if address.id == ...:
                address.delete()

    def add_avatar(self: Self) -> None:
        avatar: Avatar = Avatar.create(uow=self.uow)
        self.avatars.append(avatar)

    def delete_avatar(self: Self):
        for avatar in self.avatars:
            if avatar.id == ...:
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
