
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.unit_of_work import UnitOfWork
from app.domain.common.uowed import UowedEntity
from app.infrastructure.database.postgres.interfaces.registry import Registry


class UnitOfWorkImpl(UnitOfWork):
    def __init__(
        self,
        registry: Registry,
        connection: AsyncConnection,
    ) -> None:
        self.new: dict[type[UowedEntity], UowedEntity] = dict()
        self.dirty: dict[type[UowedEntity], UowedEntity] = dict()
        self.deleted: dict[type[UowedEntity], UowedEntity] = dict()
        self.registry = registry
        self.connection = connection

    def register_new(self, entity: UowedEntity) -> None:
        self.new[type(entity)] = entity

    def register_dirty(self, entity: UowedEntity) -> None:
        self.dirty[type(entity)] = entity

    def register_deleted(self, entity: UowedEntity) -> None:
        self.deleted[type(entity)]

    async def commit(self) -> None:
        for entity_type, entity in self.new.items():
            mapper = self.registry.get_mapper(entity_type)
            await mapper.add(entity)

        for entity_type, entity in self.dirty.items():
            mapper = self.registry.get_mapper(entity_type)
            await mapper.update(entity)

        for entity_type, entity in self.deleted.items():
            mapper = self.registry.get_mapper(entity_type)
            await mapper.delete(entity)

        await self.connection.execute("COMMIT")

