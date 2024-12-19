from uuid import UUID

from sqlalchemy import CursorResult, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.unit_of_work import UnitOfWork
from app.domain.profile.entities.profile import Profile
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.infrastructure.database.postgres.converters import result_to_profile_entity
from app.infrastructure.database.postgres.tables import (
    address_table,
    profile_table,
    social_netw_profile_table,
)


class ProfileRepositoryImpl(ProfileRepository):
    def __init__(
        self,
        unit_of_work: UnitOfWork,
        connection: AsyncConnection,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.connection = connection

    async def load(self, profile_id: UUID) -> Profile | None:
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

        return result_to_profile_entity(result, self.unit_of_work)

    async def load_all_user_profiles(self, profile_owner_id: UUID) -> list[Profile]:
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
            .where(profile_table.c.user_id == profile_owner_id)
        )

        cursor: CursorResult = await self.connection.execute(query, (profile_owner_id,))
        result = cursor.mappings().all()

        if result is None:
            return None

        return result_to_profile_entity(result, self.unit_of_work, False)
