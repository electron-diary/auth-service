from typing import Self

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

        self.profile: list[Profile] = profiles

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        user = cls(uow=uow, id=None)
        user.mark_new()

        return user
    
    def add_profile(self: Self) -> None:
        profile = Profile.create(uow=self.uow)
        self.profile.append(profile)

    def delete_profile(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.delete()

    def add_avatar(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.add_avatar()

    def delete_avatar(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.delete_avatar()

    def add_social_network(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.add_social_network()

    def delete_social_network(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.delete_social_network()

    def add_address(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.add_address()

    def delete_address(self: Self) -> None:
        for profile in self.profile:
            if profile.id == ...:
                profile.delete_address()

    def delete(self: Self) -> None:
        self.mark_deleted()
        for profile in self.profile:
            profile.delete()
