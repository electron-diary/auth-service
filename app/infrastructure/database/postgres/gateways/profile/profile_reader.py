from typing import Self
from uuid import UUID

from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.profile.dtos.profile_dto import ProfileDto
from app.application.profile.protocols.profile_reader import ProfileReaderInterface


class ProfileReaderImpl(ProfileReaderInterface):
    def __init__(
        self: Self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def get_profile_by_id(self: Self, profile_id: UUID) -> ProfileDto | None:
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
        cursor: CursorResult = await self.connection.execute(query, (profile_id, ))
        result = await cursor.fetchone()

        if result is None:
            return None

        return ProfileDto(...)

    async def get_user_profiles(self: Self, user_id: UUID) -> list[ProfileDto]:
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
        cursor: CursorResult = await self.connection.execute(query, (user_id,))
        result = await cursor.fetchall()

        if result is None:
            return None

        return ...

