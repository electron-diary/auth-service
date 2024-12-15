from typing import Self

from app.application.user.dtos.user_dto import UserDto
from app.application.user.protocols.user_reader import UserReader
from app.application.user.queries.get_by_username import GetUserByUsernameQuery


class GetUserByUsername:
    def __init__(
        self: Self,
        user_reader: UserReader,
    ) -> None:
        self.user_reader = user_reader

    async def handle(self: Self, query: GetUserByUsernameQuery) -> UserDto:
        user = await self.user_reader.get_by_username(query.username)

        return user
