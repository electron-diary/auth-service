from typing import Self
from uuid import UUID

from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.unit_of_work import UnitOfWork
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository
from app.infrastructure.database.postgres.converters.user_converters import result_to_user_entity


class UserRepositoryImpl(UserRepository):
    def __init__(
        self: Self,
        connection: AsyncConnection,
        uow: UnitOfWork,
    ) -> None:
        self.connection = connection
        self.unit_of_work = uow

    async def load(self: Self, user_id: UUID) -> User | None:
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

        return result_to_user_entity(result, self.unit_of_work)

    async def check_email_exists(self: Self, email: str) -> User | None:
        query = """
            SELECT
                user_id,
                email,
                phone_number,
                username,
                status
            FROM users
            WHERE email = ?
        """
        cursor: CursorResult = await self.connection.execute(query, (email, ))
        result = await cursor.fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)

    async def check_phone_number_exists(self: Self, phone_number: int) -> User | None:
        query = """
            SELECT
                user_id,
                email,
                phone_number,
                username,
                status
            FROM users
            WHERE phone_number = ?
        """
        cursor: CursorResult = await self.connection.execute(query, (phone_number,))
        result = await cursor.fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)

    async def check_username_exists(self: Self, username: str) -> User | None:
        query = """
            SELECT
                user_id,
                email,
                phone_number,
                username,
                status
            FROM users
            WHERE username = ?
        """
        cursor: CursorResult = await self.connection.execute(query, (username, ))
        result = await cursor.fetchone()

        if result is None:
            return None

        return result_to_user_entity(result, self.unit_of_work)

