from typing import Self

from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class Avatar(UowedEntity[None]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: ...,
    ) -> None:
        super().__init__(uow=uow, id=id)

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        avatar = cls(uow=uow, id=None)
        avatar.mark_new()

        return avatar

    def delete(self: Self) -> None:
        self.mark_deleted()
