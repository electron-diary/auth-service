from typing import Self

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class Profile(UowedEntity[None]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: ...,
    ) -> None:
        super().__init__(uow=uow, id=id)

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        profile = cls(uow=uow, id=None)
        profile.mark_new()

        return profile

    def delete(self: Self) -> None:
        self.mark_deleted()
