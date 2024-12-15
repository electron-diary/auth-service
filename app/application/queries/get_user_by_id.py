from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.application.common.user_reader import UserReader
from app.application.dto.user_dto import UserDto


@dataclass(frozen=True)
class GetUserByIdQuery:
    user_id: UUID


class GetUserById:
    def __init__(
        self: Self,
        user_reader: UserReader,
    ) -> None:
        self.user_reader = user_reader

    async def handle(self: Self, query: GetUserByIdQuery) -> UserDto:
        user = await self.user_reader.get_user_by_id(query.id)

        return user
