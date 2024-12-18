
from sqlalchemy import delete, insert
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.profile.entities.address import Address
from app.infrastructure.database.postgres.converters import address_entity_to_dict
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.infrastructure.database.postgres.tables import address_table


class AddressDataMapper(DataMapper):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self, entity: Address) -> None:
        values = address_entity_to_dict(entity)
        stmt = insert(address_table).values(values)

        await self.connection.execute(stmt)

    async def delete(self, entity: Address) -> None:
        stmt = delete(address_table).where(address_table.c.address_id == entity.id)
        await self.connection.execute(stmt)

    async def update(self, entity: Address) -> None:
        ...
