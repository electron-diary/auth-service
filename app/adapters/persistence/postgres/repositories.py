from typing import Self
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, insert

from app.application.user.repositories import UserReaderRepository, UserWriterRepository
from app.application.user.dto import UserDTO
from app.domain.user.user import User
from app.adapters.persistence.postgres.tables import UserTable
from app.adapters.persistence.postgres.converters import user_entity_to_table, table_to_dto


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

    async def create_user(self: Self, user: User) -> UserDTO:
        user_table = user_entity_to_table(user=user)
        stmt = insert(UserTable).values(**user_table.dict())
        await self.session.execute(stmt)
    
    async def update_user(self: Self, user: User) -> UserDTO:
        user_table = user_entity_to_table(user=user)
        stmt = update(UserTable).where(UserTable.id == user.id.value).values(**user_table.dict())
        await self.session.execute(stmt)

    async def delete_user(self: Self, user_id: UUID) -> None:
        stmt = delete(UserTable).where(UserTable.id == user_id)
        await self.session.execute(stmt)
