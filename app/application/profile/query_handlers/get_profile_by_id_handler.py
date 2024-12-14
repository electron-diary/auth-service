from typing import Self

from app.application.profile.dtos.profile_dto import ProfileDto
from app.application.profile.exceptions import ProfileNotFound
from app.application.profile.protocols.profile_reader import ProfileReaderInterface
from app.application.profile.queries.get_profile_by_id import GetProfileByIdQuery


class GetProfileById:
    def __init__(
        self: Self,
        profile_reader: ProfileReaderInterface,
    ) -> None:
        self.profile_reader = profile_reader

    async def handle(self: Self, query: GetProfileByIdQuery) -> ProfileDto:
        profile = await self.profile_reader.get_profile_by_id(query.profile_id)
        if not profile:
            raise ProfileNotFound("Profile not found")

        return profile
