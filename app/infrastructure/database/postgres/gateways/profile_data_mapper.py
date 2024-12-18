from sqlalchemy import delete, insert, update
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.profile.entities.profile import Profile
from app.infrastructure.database.postgres.converters import profile_entity_to_dict
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.infrastructure.database.postgres.tables import profile_table


class ProfileDataMapper(DataMapper):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self, entity: Profile) -> None:
        values = profile_entity_to_dict(entity)
        stmt = insert(profile_table).values(values)

        await self.connection.execute(stmt)

    async def update(self, entity: Profile) -> None:
        values = profile_entity_to_dict(entity)
        stmt = update(profile_table).where(profile_table.c.profile_id == entity.id).values(values)

        await self.connection.execute(stmt)

    async def delete(self, entity: Profile) -> None:
        stmt = delete(profile_table).where(profile_table.c.profile_id == entity.id)

        await self.connection.execute(stmt)
