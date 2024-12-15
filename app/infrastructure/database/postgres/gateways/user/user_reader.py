from typing import Self
from uuid import UUID

from sqlalchemy import CursorResult
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.user.dtos.user_dto import UserDto
from app.application.user.protocols.user_reader import UserReaderInterface
from app.infrastructure.database.postgres.converters.user_converters import result_to_dto


class UserReaderImpl(UserReaderInterface):
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

    async def get_by_email(self: Self, email: str) -> UserDto | None:
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

        return result_to_dto(result)

    async def get_by_phone_number(self: Self, phone_number: int) -> UserDto | None:
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

        return result_to_dto(result)

    async def get_by_username(self: Self, username: str) -> UserDto | None:
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

        return result_to_dto(result)

