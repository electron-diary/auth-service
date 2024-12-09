from typing import Self

from app.domain.unit_of_work import UnitOfWorkInterface


class UowedEntity[EntityId]:
    def __init__(self: Self, uow: UnitOfWorkInterface, id: EntityId) -> None:
        self.id: EntityId = id
        self.uow: UnitOfWorkInterface = uow

    def mark_new(self: Self) -> None:
        self.uow.register_new(self)

    def mark_dirty(self: Self) -> None:
        self.uow.register_dirty(self)

    def mark_deleted(self: Self) -> None:
        self.uow.register_deleted(self)

