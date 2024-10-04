from typing import Self
from sqlalchemy import select, delete, update, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.domain.user.entity import UserEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.domain.user.value_objects import UserName
from src.app.domain.user.value_objects import UserContact
from src.app.domain.user.value_objects import UserPassword
from src.app.domain.user.value_objects import UserCreatedAt
from src.app.domain.user.value_objects import UserUpdatedAt
from src.app.domain.user.value_objects import UserStatus
from src.app.domain.user.repositories import UserInterface


class SQLAlchemyUserInterfaceImpl(UserInterface):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def create_user(
        self: Self, 
        user_name: UserName, 
        user_contact: UserContact, 
        user_password: UserPassword, 
        user_status: UserStatus, 
        user_created_at: UserCreatedAt, 
        user_updated_at: UserUpdatedAt
    ) -> UserUUID:
        async with self.session as session:
            stmt = ...

    async def get_user_by_contact(
        self: Self, user_contact: UserContact
    ) -> UserEntity:
        pass

    async def get_user_by_uuid(
        self: Self, user_uuid: UserUUID
    ) -> UserEntity:
        pass
        
       