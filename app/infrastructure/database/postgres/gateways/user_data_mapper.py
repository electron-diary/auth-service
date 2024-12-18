
from sqlalchemy import delete, insert, update
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.user.entities.user import User
from app.infrastructure.database.postgres.converters import user_entity_to_dict
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.infrastructure.database.postgres.tables import user_table


class UserDataMapper(DataMapper):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self, entity: User) -> None:
        values = user_entity_to_dict(entity)
        stmt = insert(user_table).values(values)

        await self.connection.execute(stmt)

    async def update(self, entity: User) -> None:
        values = user_entity_to_dict(entity)
        stmt = update(user_table).where(user_table.c.user_id == entity.id).values(values)

        await self.connection.execute(stmt)

    async def delete(self, entity: User) -> None:
        stmt = delete(user_table).where(user_table.c.user_id == entity.id)

        await self.connection.execute(stmt)
