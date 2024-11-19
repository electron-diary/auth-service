from collections.abc import Sequence
from dataclasses import asdict
from typing import Self

from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection, AsyncIOMotorCursor

from app.application.base.event_store_interface import EventStoreInterface
from app.application.base.integration_event import IntegrationEvent
from app.domain.base.base_event import BaseDomainEvent
from app.domain.value_objects.uuid_value_object import UUIDValueObject
from app.adapters.database.mongo.converters import convert_integartion_event_to_domain_event



class EventSoreRepository(EventStoreInterface):
    def __init__(self: Self, session: AsyncIOMotorClientSession, collection: AsyncIOMotorCollection) -> None:
        self.session: AsyncIOMotorClientSession = session
        self.collection: AsyncIOMotorCollection = collection

    async def save_event(self: Self, event: Sequence[BaseDomainEvent]) -> None:
        for domain_event in event:
            integration_event: IntegrationEvent = IntegrationEvent.from_domain_to_integration_event(event=domain_event)
            await self.collection.insert_one(asdict(integration_event), session=self.session)

    async def get_events(self: Self, uuid: UUIDValueObject) -> Sequence[BaseDomainEvent]:
        list_events: list[BaseDomainEvent] = []
        cursor: AsyncIOMotorCursor = self.collection.find({"uuid": str(uuid.to_raw())})
        result: list[IntegrationEvent] = await cursor.to_list()
        for integration_event in result:
            domain_event: BaseDomainEvent = convert_integartion_event_to_domain_event(integration_event=integration_event)
            list_events.append(domain_event)
        return list_events

