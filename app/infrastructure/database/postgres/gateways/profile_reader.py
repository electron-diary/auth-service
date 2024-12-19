from uuid import UUID

from sqlalchemy import CursorResult, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.profile_reader import ProfileReader
from app.application.dto.profile_dto import ProfileDto
from app.infrastructure.database.postgres.converters import result_to_profile_dto
from app.infrastructure.database.postgres.tables import (
    address_table,
    profile_table,
    social_netw_profile_table,
)


class ProfileReaderImpl(ProfileReader):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def get_profile_by_id(self, profile_id: UUID) -> ProfileDto | None:
        query = (
            select(
                profile_table,
                address_table,
                social_netw_profile_table,
            )
            .join(
                address_table,
                profile_table.c.profile_id == address_table.c.profile_id,
                isouter=True,
            )
            .join(
                social_netw_profile_table,
                profile_table.c.profile_id == social_netw_profile_table.c.profile_id,
                isouter=True,
            )
            .where(profile_table.c.profile_id == profile_id)
        )

        cursor: CursorResult = await self.connection.execute(query)
        result = cursor.mappings().unique().all()

        if not result:
            return None

        return result_to_profile_dto(rows=result)

    async def get_user_profiles(self, user_id: UUID) -> list[ProfileDto]:
        query = (
            select(
                profile_table,
                address_table,
                social_netw_profile_table,
            )
            .join(
                address_table,
                profile_table.c.profile_id == address_table.c.profile_id,
                isouter=True,
            )
            .join(
                social_netw_profile_table,
                profile_table.c.profile_id == social_netw_profile_table.c.profile_id,
                isouter=True,
            )
            .where(profile_table.c.user_id == user_id)
        )

        cursor: CursorResult = await self.connection.execute(query)
        result = cursor.mappings().unique().all()

        if result is None:
            return None

        return result_to_profile_dto(rows=result, get_first=False)

