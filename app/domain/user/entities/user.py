from typing import Self

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity
from app.domain.user.entities.profile import Profile


class User(UowedEntity[None]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: ...,
        profile: Profile,
    ) -> None:
        super().__init__(uow=uow, id=id)

        self.profile: Profile = profile

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        user = cls(uow=uow, id=None)
        user.mark_new()

        return user

    def add_avatar(self: Self) -> None:
        self.profile.add_avatar()

    def delete_avatar(self: Self) -> None:
        self.profile.delete_avatar()

    def add_social_network(self: Self) -> None:
        self.profile.add_social_network()

    def delete_social_network(self: Self) -> None:
        self.profile.delete_social_network()

    def add_address(self: Self) -> None:
        self.profile.add_address()

    def delete_address(self: Self) -> None:
        self.profile.delete_address()

    def delete(self: Self) -> None:
        self.profile.delete()
        self.mark_deleted()
