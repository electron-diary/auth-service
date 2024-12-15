from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.application.common.profile_reader import ProfileReader
from app.application.dto.profile_dto import ProfileDto


@dataclass(frozen=True)
class GetProfileByIdQuery:
    profile_id: UUID


class GetProfileById:
    def __init__(
        self: Self,
        profile_reader: ProfileReader,
    ) -> None:
        self.profile_reader = profile_reader

    async def handle(self: Self, query: GetProfileByIdQuery) -> ProfileDto | None:
        profile = await self.profile_reader.get_profile_by_id(query.profile_id)

        return profile
