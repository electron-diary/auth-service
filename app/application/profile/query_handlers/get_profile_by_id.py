from typing import Self

from app.application.profile.dtos.profile_dto import ProfileDto
from app.application.profile.protocols.profile_reader import ProfileReader
from app.application.profile.queries.get_profile_by_id import GetProfileByIdQuery


class GetProfileById:
    def __init__(
        self: Self,
        profile_reader: ProfileReader,
    ) -> None:
        self.profile_reader = profile_reader

    async def handle(self: Self, query: GetProfileByIdQuery) -> ProfileDto | None:
        profile = await self.profile_reader.get_profile_by_id(query.profile_id)

        return profile
