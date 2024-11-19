from collections.abc import Sequence
from dataclasses import asdict
from typing import Self

from motor.motor_asyncio import AsyncIOMotorClientSession, AsyncIOMotorCollection

from app.adapters.database.mongo.converters import convert_domain_event_to_mongo_event
from app.adapters.database.mongo.payloads import MongoEvent
from app.application.base.event_store_interface import EventStoreInterface
from app.domain.base.base_event import BaseDomainEvent
from app.domain.value_objects.uuid_value_object import UUIDValueObject


class EventSoreRepository(EventStoreInterface):
    def __init__(self: Self, session: AsyncIOMotorClientSession, collection: AsyncIOMotorCollection) -> None:
        self.session: AsyncIOMotorClientSession = session
        self.collection: AsyncIOMotorCollection = collection

    async def save_event(self: Self, event: Sequence[BaseDomainEvent]) -> None:
        for domain_event in event:
            mongo_event: MongoEvent = convert_domain_event_to_mongo_event(event=domain_event)
            await self.collection.insert_one(asdict(mongo_event), session=self.session)

    async def get_current_state(self: Self, uuid: UUIDValueObject) -> Sequence[BaseDomainEvent]:
        # list_events: list[BaseDomainEvent] = []
        # cursor: AsyncIOMotorCursor = self.collection.find({"uuid": str(uuid.to_raw())})
        # result: Sequence[MongoEvent] = await cursor.to_list()
        # for mongo_event in result:
        #     list_events.append(mongo_event)
        # return list_events
        ...
