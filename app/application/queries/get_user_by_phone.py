from dataclasses import dataclass
from typing import Self

from app.application.common.user_reader import UserReader
from app.application.dto.user_dto import UserDto


@dataclass(frozen=True)
class GetUserByPhoneQuery:
    phone: int


class GetUserByPhone:
    def __init__(
        self: Self,
        user_reader: UserReader,
    ) -> None:
        self.user_reader = user_reader

    async def handle(self: Self, query: GetUserByPhoneQuery) -> UserDto:
        user = await self.user_reader.get_by_phone_number(query.phone_number)

        return user
