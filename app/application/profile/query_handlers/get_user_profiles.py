from typing import Self

from app.application.profile.dtos.profile_dto import ProfileDto
from app.application.profile.exceptions import ProfileNotFound
from app.application.profile.protocols.profile_reader import ProfileReaderInterface
from app.application.profile.queries.get_user_profiles import GetUserProfilesQuery


class GetUserProfiles:
    def __init__(
        self: Self,
        profile_reader:
        ProfileReaderInterface,
    ) -> None:
        self.profile_reader = profile_reader

    async def handle(self: Self, query: GetUserProfilesQuery) -> list[ProfileDto]:
        profiles = await self.profile_reader.get_user_profiles(query.user_id)
        if not profiles:
            raise ProfileNotFound("Profiles not found")

        return profiles
