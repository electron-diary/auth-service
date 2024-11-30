from typing import Self
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection

from app.application.user.interfaces import UserReaderGatewayInterface, UserProjectionsGatewayInterface
from app.application.user.dtos import UserDTO
from app.domain.user.actions import UserCreated, UserDeleted, UsernameUpdated, UserRestored, ContactsUpdated


class UserProjectionsGatewayImpl(UserProjectionsGatewayInterface):
    def __init__(self: Self, collection: AsyncIOMotorCollection, session: AsyncIOMotorClientSession) -> None:
        self.session: AsyncIOMotorClientSession = session
        self.collection: AsyncIOMotorCollection = collection

    async def add_user(self: Self, event: UserCreated) -> None:
        await self.collection.insert_one(
            document={
                "user_id": event.user_id,
                "username": event.username,
                "phone_number": event.phone_number,
                "is_deleted": event.is_deleted
            }
        )
    
    async def delete_user(self: Self, event: UserDeleted) -> None:
        await self.collection.update_one(
            filter={"user_id": event.user_id},
            update={"$set": {"is_deleted": event.is_deleted}}
        )

    async def update_username(self: Self, event: UsernameUpdated) -> None:
        await self.collection.update_one(
            filter={"user_id": event.user_id},
            update={"$set": {"username": event.username}}
        )

    async def update_contacts(self: Self, event: ContactsUpdated) -> None:
        await self.collection.update_one(
            filter={"user_id": event.user_id},
            update={"$set": {"phone_number": event.phone_number}}
        )

    async def restore_user(self: Self, event: UserRestored) -> None:
        await self.collection.update_one(
            filter={"user_id": event.user_id},
            update={"$set": {"is_deleted": event.is_deleted}}
        )


class UserReaderGatewayImpl(UserReaderGatewayInterface):
    def __init__(self: Self, collection: AsyncIOMotorCollection, session: AsyncIOMotorClientSession) -> None:
        self.session: AsyncIOMotorClientSession = session
        self.collection: AsyncIOMotorCollection = collection

    async def get_user_by_id(self: Self, user_id: UUID) -> None:
        statement = {"user_id": user_id}
        user: dict[str] | None = await self.collection.find_one(filter=statement, projection={"_id": 0})
        if not user:
            return None
        return UserDTO(**user)
