from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.vos.cocial_networks.link import SocialNetworkLink
from app.domain.user.vos.cocial_networks.type import SocialNetworkType
from app.domain.user.vos.user.id import Id


class SocialNetwork(UowedEntity[Id]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: Id,
        type: SocialNetworkType,
        link: SocialNetworkLink,
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.social_network_type: SocialNetworkType = type
        self.social_network_link: SocialNetworkLink = link

    @classmethod
    def create(
        cls: type[Self], 
        uow: UnitOfWorkInterface,
        social_network_id: UUID,
        social_network_type: str,
        social_network_link: str,
    ) -> Self:
        social_network = cls(
            uow=uow, 
            id=Id(social_network_id),
            type=SocialNetworkType(social_network_type),
            link=SocialNetworkLink(social_network_link),
        )
        social_network.mark_new()

        return social_network

    def delete(self: Self) -> None:
        self.mark_deleted()
