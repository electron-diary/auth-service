from typing import Self
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.database.postgres.mappers import convert_user_table_to_dto
from app.adapters.database.postgres.tables.user_table import UserTable
from app.application.dto.user_dto import UserDto
from app.application.interfaces.user_queries_repository import UserQueriesRepository


class UserReaderRepository(UserQueriesRepository):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_user_by_id(self: Self, uuid: UUID) -> UserDto:
        query = select(UserTable).where(UserTable.uuid == uuid)
        result = await self.session.execute(query)
        if not result:
            return None
        user_table: UserTable = result.scalars().one()
        dto: UserDto = convert_user_table_to_dto(user_table=user_table)
        return dto
