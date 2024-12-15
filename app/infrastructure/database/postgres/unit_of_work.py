from typing import Self

from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.registry import RegistryInterface
from app.application.unit_of_work import UnitOfWorkInterface
from app.domain.uowed import UowedEntity


class UnitOfWorkImpl(UnitOfWorkInterface):
    def __init__(
        self: Self,
        registry: RegistryInterface,
        connection: AsyncConnection,
    ) -> None:
        self.new: dict[type[UowedEntity], list[UowedEntity]] = dict()
        self.dirty: dict[type[UowedEntity], list[UowedEntity]] = dict()
        self.deleted: dict[type[UowedEntity], list[UowedEntity]] = dict()
        self.registry = registry
        self.connection = connection

    def register_new(self: Self, entity: UowedEntity) -> None:
        self.new.setdefault(type(entity), list()).append(entity)

    def register_dirty(self: Self, entity: UowedEntity) -> None:
        self.dirty.setdefault(type(entity), list()).append(entity)

    def register_deleted(self: Self, entity: UowedEntity) -> None:
        self.deleted.setdefault(type(entity), list()).append(entity)

    async def commit(self: Self) -> None:
        for entity_type, entity in self.new.values():
            mapper = self.registry.get_mapper(entity_type)
            await mapper.add(entity)

        for entity_type, entity in self.dirty.values():
            mapper = self.registry.get_mapper(entity_type)
            await mapper.update(entity)

        for entity_type, entity in self.deleted.values():
            mapper = self.registry.get_mapper(entity_type)
            await mapper.delete(entity)

        await self.connection.execute("COMMIT")

