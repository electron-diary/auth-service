from uuid import UUID

from sqlalchemy import CursorResult, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.unit_of_work import UnitOfWork
from app.domain.profile.entities.profile import Profile
from app.domain.profile.repositories.profile_repository import ProfileRepository
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
                profile_table.c.profile_id,
                profile_table.c.user_ud,
                profile_table.c.first_name,
                profile_table.c.last_name,
                profile_table.c.middle_name,
                profile_table.c.bio,
                profile_table.c.status,
                address_table.c.address_id,
                address_table.c.country,
                address_table.c.city,
                address_table.c.street,
                address_table.c.house_number,
                address_table.c.apartament_number,
                address_table.c.postal_code,
                social_netw_profile_table.c.social_netw_profile_id,
                social_netw_profile_table.c.social_netw_profile_name,
                social_netw_profile_table.c.social_netw_profile_link,
            )
            .join(
                profile_table,
                address_table,
                isouter=True,
            )
            .join(
                profile_table,
                social_netw_profile_table,
                isouter=True,
            )
            .where(profile_table.c.profile_id == profile_id)
        )

        cursor: CursorResult = await self.connection.execute(query)
        result = await cursor.fetchone()

        if not result:
            return None

        print(result)
        return None

    async def load_all_user_profiles(self, profile_owner_id: UUID) -> list[Profile]:
        query = (
            select(
                profile_table.c.profile_id,
                profile_table.c.user_id,
                profile_table.c.first_name,
                profile_table.c.last_name,
                profile_table.c.middle_name,
                profile_table.c.bio,
                profile_table.c.status,
                address_table.c.address_id,
                address_table.c.country,
                address_table.c.city,
                address_table.c.street,
                address_table.c.house_number,
                address_table.c.apartament_number,
                address_table.c.postal_code,
                social_netw_profile_table.c.social_netw_profile_id,
                social_netw_profile_table.c.social_netw_profile_name,
                social_netw_profile_table.c.social_netw_profile_link,
            )
            .join(
                profile_table,
                address_table,
                isouter=True,
            )
            .join(
                profile_table,
                social_netw_profile_table,
                isouter=True,
            )
            .where(profile_table.c.user_id == profile_owner_id)
        )

        cursor: CursorResult = await self.connection.execute(query, (profile_owner_id,))
        result = await cursor.fetchall()

        if result is None:
            return None

        print(result)
        return []
