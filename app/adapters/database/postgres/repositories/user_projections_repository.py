from typing import Self

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, insert

from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.adapters.database.postgres.tables.user_table import UserTable
from app.adapters.database.postgres.mappers import convert_user_create_event_to_table
from app.application.interfaces.user_projections_repository import UserProjectionsRepository


class UserProjectionsRepositoryImpl(UserProjectionsRepository):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def create_user(self: Self, event: CreateUserEvent) -> None:
        user_model: UserTable = convert_user_create_event_to_table(event=event)
        stmt = insert(UserTable).values(user_model)
        await self.session.execute(stmt)

    async def update_user_fullname(self: Self, event: UpdateUserFullNameEvent) -> None:
        stmt = update(UserTable).where(UserTable.uuid == event.uuid).values(
            first_name=event.new_user_first_name,
            last_name=event.new_user_last_name,
            middle_name=event.new_user_middle_name,
        )
        await self.session.execute(stmt)

    async def update_user_contact(self: Self, event: UpdateUserContactEvent) -> None:
        stmt = update(UserTable).where(UserTable.uuid == event.uuid).values(
            user_phone=event.new_user_phone,
            user_email=event.new_user_email,
        )
        await self.session.execute(stmt)

    async def delete_user(self: Self, event: DeleteUserEvent) -> None:
        stmt = delete(UserTable).where(UserTable.uuid == event.uuid)
        await self.session.execute(stmt)