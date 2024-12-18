
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.profile.entities.profile import Profile
from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper


class ProfileDataMapper(DataMapper):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self, entity: Profile) -> None:
        stmt = """
            INSERT INTO profiles
                profile_id,
                profile_owner_id,
                first_name,
                last_name,
                middle_name,
                bio,
                status 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        await self.connection.execute(
            stmt,
            (
                entity.id,
                entity.profile_owner_id,
                entity.fullname.first_name,
                entity.fullname.last_name,
                entity.fullname.middle_name,
                entity.bio,
                entity.status,
            ),
        )

    async def update(self, entity: Profile) -> None:
        stmt = """
            UPDATE profiles
            SET
                profile_owner_id = ?,
                first_name = ?,
                last_name = ?,
                middle_name = ?,
                bio = ?,
                status = ?
            WHERE profile_id = ?
        """
        await self.connection.execute(
            stmt,
            (
                entity.profile_owner_id,
                entity.fullname.first_name,
                entity.fullname.last_name,
                entity.fullname.middle_name,
                entity.bio,
                entity.status,
                entity.id,
            ),
        )

    async def delete(self, entity: Profile) -> None:
        stmt = """
            DELETE FROM profiles
            WHERE profile_id = ?
        """
        await self.connection.execute(stmt, (entity.id, ))
