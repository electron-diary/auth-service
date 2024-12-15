from typing import Self

from app.application.common.event_bus import EventBus
from app.domain.common.domain_event import DomainEvent
from app.infrastructure.brokers.interfaces import MessagePublisher


class EventBusImpl(EventBus):
    def __init__(
        self: Self,
        message_publisher: MessagePublisher,
    ) -> None:
        self.message_publisher = message_publisher

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            await self.message_publisher.publish(...)
