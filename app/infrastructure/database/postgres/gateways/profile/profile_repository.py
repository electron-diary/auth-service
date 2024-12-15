from typing import Self
from uuid import UUID

from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.unit_of_work import UnitOfWorkInterface
from app.domain.profile.entities.profile import Profile
from app.domain.profile.repositories.profile_repository import ProfileRepository


class ProfileRepositoryImpl(ProfileRepository):
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkInterface,
        connection: AsyncConnection,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.connection = connection

    async def load(self: Self, profile_id: UUID) -> Profile | None:
        query = """
            SELECT 
                profiles.profile_id, 
                profiles.owner_id, 
                profiles.first_name
                profiles.last_name, 
                profiles.middle_name, 
                profiles.bio, 
                profiles.status,
                social_netw_profiles.social_netw_profile_owner_id,
                social_netw_profiles.social_netw_profile_id,
                social_netw_profiles.social_netw_profile_name
                social_netw_profiles.social_netw_profile_link
                addresses.address_id,
                addresses.address_owner_id
                addresses.country,
                addresses.city,
                addresses.street,
                addresses.house_number,
                addresses.apartment_number,
                addresses.postal_code
            FROM profiles
            JOIN social_netw_profiles ON social_netw_profiles.social_netw_profile_owner_id = profiles.profile_id
            JOIN addresses ON addresses.address_owner_id = profiles.profile_id
            WHERE profiles.profile_id = ?
        """
        cursor: CursorResult = await self._connection.execute(query, (profile_id, ))
        result = await cursor.fetchone()

        if result is None:
            return None

        return Profile(uow=self.unit_of_work)

    async def load_all_user_profiles(self: Self, profile_owner_id: UUID) -> list[Profile]:
        query = """
            SELECT
                profiles.profile_id,
                profiles.owner_id,
                profiles.first_name
                profiles.last_name,
                profiles.middle_name,
                profiles.bio,
                profiles.status,
                social_netw_profiles.social_netw_profile_owner_id,
                social_netw_profiles.social_netw_profile_id,
                social_netw_profiles.social_netw_profile_name
                social_netw_profiles.social_netw_profile_link
                addresses.address_id,
                addresses.address_owner_id
                addresses.country,
                addresses.city,
                addresses.street,
                addresses.house_number,
                addresses.apartment_number,
                addresses.postal_code
            FROM profiles
            JOIN social_netw_profiles ON social_netw_profiles.social_netw_profile_owner_id = profiles.profile_id
            JOIN addresses ON addresses.address_owner_id = profiles.profile_id
            WHERE profiles.owner_id = ?
        """
        cursor: CursorResult = await self._connection.execute(query, (profile_owner_id,))
        result = await cursor.fetchall()

        if result is None:
            return None

        return ...
