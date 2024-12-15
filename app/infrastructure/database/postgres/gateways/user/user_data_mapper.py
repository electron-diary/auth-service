from typing import Self

from sqlalchemy.ext.asyncio import AsyncConnection

from app.infrastructure.database.postgres.interfaces.data_mapper import DataMapper
from app.domain.user.entities.user import User


class UserDataMapper(DataMapper):
    def __init__(
        self: Self,
        connection: AsyncConnection,
    ) -> None:
        self.connection = connection

    async def add(self: Self, entity: User) -> None:
        stmt = """
            INSERT INTO users (user_id, email, phone_number, username, status)
            VALUES (?, ?, ?, ?, ?)
        """
        await self.connection.execute(
            stmt,
            (
                entity.id,
                entity.contacts.email,
                entity.contacts.phone_number,
                entity.username,
                entity.status,
            ),
        )

    async def update(self: Self, entity: User) -> None:
        stmt = """
            UPDATE users
            SET email = ?, phone_number = ?, username = ?, status = ?
            WHERE user_id = ?
        """
        await self.connection.execute(
            stmt,
            (
                entity.contacts.email,
                entity.contacts.phone_number,
                entity.username,
                entity.status,
                entity.user_id,
            ),
        )

    async def delete(self: Self, entity: User) -> None:
        stmt = """
            DELETE FROM users
            WHERE user_id = ?
        """
        await self.connection.execute(stmt, (entity.user_id, ))
