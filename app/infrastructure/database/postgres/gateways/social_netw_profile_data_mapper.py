from typing import Self

from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.profile.entities.social_netw_profile import SocialNetwProfile
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper


class SocialNetwProfileDataMapper(DataMapper):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self, entity: SocialNetwProfile) -> None:
        stmt = """
            INSERT INTO social_netw_profiles
                social_netw_profile_id,
                social_netw_profile_owner_id,
                social_netw_profile_name,
                social_netw_profile_link
            VALUES (?, ?, ?, ?)
        """
        await self.connection.execute(
            stmt,
            (
                entity.id,
                entity.profile_id,
                entity.social_netw_name,
                entity.social_profile_link,
            ),
        )

    async def delete(self, entity: SocialNetwProfile) -> None:
        stmt = """
            DELETE FROM social_netw_profiles
            WHERE social_netw_profile_id = ?
        """
        await self.connection.execute(stmt, (entity.id, ))

    async def update(self: Self, entity: SocialNetwProfile) -> None:
        pass
