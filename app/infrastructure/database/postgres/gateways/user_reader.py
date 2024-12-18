from uuid import UUID

from sqlalchemy import CursorResult, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.user_reader import UserReader
from app.application.dto.user_dto import UserDto
from app.infrastructure.database.postgres.converters import result_to_user_dto
from app.infrastructure.database.postgres.tables import user_table


class UserReaderImpl(UserReader):
    def __init__(
        self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def get_user_by_id(self, user_id: UUID) -> UserDto | None:
        query = select(user_table).where(user_table.c.user_id == user_id)
        cursor: CursorResult = await self.connection.execute(query)

        result = await cursor.fetchone()

        if result is None:
            return None

        return result_to_user_dto(result)
