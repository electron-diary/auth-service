from collections.abc import Sequence
from typing import Self

from app.adapters.broker.interfaces import KafkaBrokerInterface
from app.application.base.event_bus_interface import EventBusInterface
from app.domain.base.base_event import BaseDomainEvent


class EventBusRepository(EventBusInterface):
    def __init__(self: Self, broker: KafkaBrokerInterface) -> None:
        self.broker: KafkaBrokerInterface = broker

    async def send_event(self: Self, event: Sequence[BaseDomainEvent]) -> None:
        for _domain_event in event:
            await self.broker.produce_messages(

            )
