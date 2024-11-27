from typing import Self
from uuid import UUID

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.user.dto import UserDTO
from app.application.user.repositories import UserReaderRepository, UserWriterRepository
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username
from app.infrastructure.persistence.postgres.converters import table_to_dto, user_entity_to_table
from app.infrastructure.persistence.postgres.tables import UserTable


class UserReaderImpl(UserReaderRepository):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_user_by_id(self: Self, user_id: UUID) -> UserDTO:
        stmt = select(UserTable).where(UserTable.id == user_id)
        user = await self.session.execute(stmt)
        if user is None:
            return None
        result: UserTable = user.scalars().one()
        return table_to_dto(user=result)

    async def get_users(self: Self) -> list[UserDTO]:
        stmt = select(UserTable)
        users = await self.session.execute(stmt)
        if not users:
            return None
        result = list[UserTable] = users.scalars().all()
        return [table_to_dto(user=user) for user in result]


class UserWriterImpl(UserWriterRepository):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def save_user(self: Self, user: User) -> UserDTO:
        user_table = user_entity_to_table(user=user)
        stmt = insert(UserTable).values(user_table.to_dict())
        await self.session.execute(stmt)

    async def delete_user(self: Self, user_id: UserId, is_deleted: DeletedUser) -> None:
        stmt = update(UserTable).where(UserTable.id == user_id.value).values(is_deleted=is_deleted.value)
        await self.session.execute(stmt)

    async def restore_user(self, user_id: UserId, is_deleted: DeletedUser) -> None:
        stmt = update(UserTable).where(UserTable.id == user_id.value).values(is_deleted=is_deleted.value)
        await self.session.execute(stmt)

    async def update_contacts(self, user_id: UserId, contacts: Contacts) -> None:
        stmt = update(UserTable).where(UserTable.id == user_id.value).values(
            email=contacts.email, phone_number=contacts.phone,
        )
        await self.session.execute(stmt)

    async def update_username(self, user_id: UserId, username: Username) -> None:
        stmt = update(UserTable).where(UserTable.id == user_id.value).values(username=username.value)
        await self.session.execute(stmt)
