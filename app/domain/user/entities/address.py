from typing import Self

from app.domain.uowed import UowedEntity
from app.domain.unit_of_work import UnitOfWorkInterface


class Address(UowedEntity[None]):
    def __init__(
        self: Self,
        uow: UnitOfWorkInterface,
        id: ...,
    ) -> None:
        super().__init__(uow=uow, id=id)

    @classmethod
    def create(cls: type[Self], uow: UnitOfWorkInterface) -> Self:
        address = cls(uow=uow, id=None)
        address.mark_new()

        return address

    def delete(self: Self) -> None:
        self.mark_deleted()