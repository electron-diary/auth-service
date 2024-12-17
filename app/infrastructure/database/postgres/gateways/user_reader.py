from typing import Self
from uuid import UUID

from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.user_reader import UserReader
from app.application.dto.user_dto import UserDto
from app.infrastructure.database.postgres.converters.user_converters import result_to_dto


class UserReaderImpl(UserReader):
    def __init__(
        self: Self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def get_user_by_id(self: Self, user_id: UUID) -> UserDto | None:
        query = """
            SELECT 
                user_id,
                email,
                phone_number,
                username,
                status 
            FROM users 
            WHERE user_id = ?
        """
        cursor: CursorResult = await self.connection.execute(query, (user_id,))
        result = await cursor.fetchone()

        if result is None:
            return None

        return result_to_dto(result)
