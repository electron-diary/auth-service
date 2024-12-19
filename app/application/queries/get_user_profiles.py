from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.application.common.profile_reader import ProfileReader
from app.application.dto.profile_dto import ProfileDto


@dataclass(frozen=True)
class GetUserProfilesQuery:
    profile_owner_id: UUID


class GetUserProfiles:
    def __init__(
        self,
        profile_reader: ProfileReader,
    ) -> None:
        self.profile_reader = profile_reader

    async def handle(self: Self, query: GetUserProfilesQuery) -> list[ProfileDto]:
        profiles = await self.profile_reader.get_user_profiles(query.profile_owner_id)

        return profiles
