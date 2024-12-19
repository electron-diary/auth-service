from typing import Self
from uuid import UUID

from sqlalchemy import CursorResult, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.unit_of_work import UnitOfWork
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository
from app.infrastructure.database.postgres.converters import result_to_user_entity
from app.infrastructure.database.postgres.tables import user_table


class UserRepositoryImpl(UserRepository):
    def __init__(
        self,
        connection: AsyncConnection,
        uow: UnitOfWork,
    ) -> None:
        self.connection = connection
        self.unit_of_work = uow

    async def load(self, user_id: UUID) -> User | None:
        query = select(user_table).where(user_table.c.user_id == user_id)
        cursor: CursorResult = await self.connection.execute(query)

        result = cursor.mappings().fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)

    async def check_email_exists(self, email: str) -> User | None:
        query = select(user_table).where(user_table.c.email == email)
        cursor: CursorResult = await self.connection.execute(query)

        result = cursor.mappings().fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)

    async def check_phone_number_exists(self, phone_number: int) -> User | None:
        query = select(user_table).where(user_table.c.phone_number == phone_number)
        cursor: CursorResult = await self.connection.execute(query)

        result = cursor.mappings().fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)

    async def check_username_exists(self: Self, username: str) -> User | None:
        query = select(user_table).where(user_table.c.username == username)
        cursor: CursorResult = await self.connection.execute(query)

        result = cursor.mappings().fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)


