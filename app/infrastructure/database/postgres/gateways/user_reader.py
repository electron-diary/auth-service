from uuid import UUID

from sqlalchemy import CursorResult, text
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.user_reader import UserReader
from app.application.dto.user_dto import UserDto
from app.infrastructure.database.postgres.converters.user_converters import result_to_dto


class UserReaderImpl(UserReader):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def get_user_by_id(self, user_id: UUID) -> UserDto | None:
        query = "SELECT * FROM users(:user_id)"
        cursor: CursorResult = await self.connection.execute(text(query), {"user_id": user_id})
        result = await cursor.fetchone()

        if result is None:
            return None

        return result_to_dto(result)
