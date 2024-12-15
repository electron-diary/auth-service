from typing import Self

from app.domain.common.unit_of_work import UnitOfWorkTracker


class UowedEntity[EntityId]:
    def __init__(self: Self, uow: UnitOfWorkTracker, id: EntityId) -> None:
        self.id: EntityId = id
        self.uow = uow

    def mark_new(self: Self) -> None:
        self.uow.register_new(self)

    def mark_dirty(self: Self) -> None:
        self.uow.register_dirty(self)

    def mark_deleted(self: Self) -> None:
        self.uow.register_deleted(self)

