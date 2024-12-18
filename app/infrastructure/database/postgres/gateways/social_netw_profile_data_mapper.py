from typing import Self

from sqlalchemy import delete, insert
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.profile.entities.social_netw_profile import SocialNetwProfile
from app.infrastructure.database.postgres.converters import social_netw_profile_entity_to_dict
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.infrastructure.database.postgres.tables import profile_table


class SocialNetwProfileDataMapper(DataMapper):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self, entity: SocialNetwProfile) -> None:
        values = social_netw_profile_entity_to_dict(entity)
        stmt = insert(profile_table).values(values)

        await self.connection.execute(stmt)

    async def delete(self, entity: SocialNetwProfile) -> None:
        stmt = delete(profile_table).where(profile_table.c.social_netw_profile_id == entity.id)

        await self.connection.execute(stmt)

    async def update(self: Self, entity: SocialNetwProfile) -> None:
        pass
