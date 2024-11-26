from typing import Self, Any
from dataclasses import asdict
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection, AsyncIOMotorCursor

from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User
from app.application.base.event_store import EventStoreRepository



class EventStoreImpl(EventStoreRepository):
    def __init__(
        self: Self, collection: AsyncIOMotorCollection, session: AsyncIOMotorClientSession
    ) -> None:
        self.collection: AsyncIOMotorCollection = collection
        self.session: AsyncIOMotorClientSession = session

    async def save_event(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            await self.collection.insert_one(asdict(obj=event), session=self.session)

    async def get_events(self: Self, id: UUID) -> list[DomainEvent]:
        stmt: dict[str | Any] = dict(uuid=id)
        cursor: AsyncIOMotorCursor = self.collection.find(stmt)
        events: list[DomainEvent] = await cursor.to_list(length=None)
        return ...
    
    async def get_current_state(self: Self, id: UUID) -> User:
        events: list[DomainEvent] = await self.get_events(id=id)
        ...
        return ...