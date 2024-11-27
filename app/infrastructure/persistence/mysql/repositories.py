from typing import Self
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from uuid import UUID

from app.application.base.event_store import EventStoreRepository
from app.domain.base.domain_event import DomainEvent
from app.domain.base.domain_entity import DomainEntity
from app.infrastructure.persistence.mysql.tables import Events
from app.infrastructure.persistence.mysql.converters import event_to_table


class EventStoreRepositoryImpl(EventStoreRepository):
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def save_event(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            table: Events = event_to_table(event=event)
            stmt = insert(Events).values(table.to_dict())
            await self.session.execute(stmt)

    async def get_events(self: Self, id: UUID) -> list[DomainEvent]:
        stmt = select(Events).where(Events.agregate_id == id)
        result: Result[Events] = await self.session.execute(stmt)
        res: list[Events] | None = result.scalars().all()
        if res is None:
            return res
        return [event.event_data for event in res]
    
    async def get_current_state(self: Self, id: UUID) -> DomainEntity:
        ...

