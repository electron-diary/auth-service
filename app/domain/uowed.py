from typing import Self

from app.domain.unit_of_work import UnitOfWork


class UowedEntity[EntityId]:
    def __init__(self: Self, uow: UnitOfWork) -> None:
        self.id: EntityId = EntityId
        self.uow: UnitOfWork = uow

    def mark_new(self: Self) -> None:
        self.uow.register_new(self)

    def mark_dirty(self: Self) -> None:
        self.uow.register_dirty(self)

