from typing import Self

from sqlalchemy import Insert, Result, Select, Update, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.user.interfaces import UserWriterGatewayInterface
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, UserId
from app.infrastructure.databases.postgres.converters import convert_user_table_to_user, convert_user_to_table
from app.infrastructure.databases.postgres.tables import UserTable


class UserWriterGatewayImpl(UserWriterGatewayInterface):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def get_user_by_id(self: Self, user_id: UserId) -> User | None:
        stmt: Select = select(UserTable).where(UserTable.id == user_id.value)
        result: Result[UserTable] = await self.session.execute(stmt)
        user: UserTable | None = result.scalars().first()
        if not user:
            return None
        return convert_user_table_to_user(user)

    async def check_phone_exist(self: Self, phone_number: Contacts) -> User | None:
        stmt: Select = select(UserTable).where(UserTable.phone_number == phone_number.phone)
        result: Result[UserTable] = await self.session.execute(stmt)
        user: UserTable | None = result.scalars().first()
        if not user:
            return None
        return convert_user_table_to_user(user)

    async def create_user(self: Self, user: User) -> bool:
        user_table: UserTable = convert_user_to_table(user)
        stmt: Insert = insert(UserTable).values(user_table.to_dict())
        await self.session.execute(stmt)

    async def update_user(self: Self, user: User) -> bool:
        user_table: UserTable = convert_user_to_table(user)
        stmt: Update = update(UserTable).where(UserTable.id == user_table.id).values(user_table.to_dict())
        await self.session.execute(stmt)
