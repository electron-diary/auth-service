from typing import Self

from app.application.user.dtos.user_dto import UserDto
from app.application.user.protocols.user_reader import UserReaderInterface
from app.application.user.exceptions import UserNotFound
from app.application.user.queries.get_by_phone_number import GetUserByPhoneQuery


class GetUserByPhone:
    def __init__(
        self: Self, 
        user_reader: UserReaderInterface
    ) -> None:
        self.user_reader = user_reader

    async def handle(self: Self, query: GetUserByPhoneQuery) -> UserDto:
        user = await self.user_reader.get_by_phone_number(query.phone_number)
        if not user:
            raise UserNotFound('User not found')
        
        return user