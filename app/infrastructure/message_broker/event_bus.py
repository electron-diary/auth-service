from typing import Self
from dataclasses import asdict

from faststream.rabbit.annotations import RabbitBroker as Broker

from app.application.base.event_queue import EventBusRepository
from app.domain.base.domain_event import DomainEvent
from app.infrastructure.message_broker.config import RabbitConfig
from app.infrastructure.events.integration_event import IntegrationEvent
from app.infrastructure.events.converters import domain_event_to_integration


class EventBusImpl(EventBusRepository):
    def __init__(self: Self, broker: Broker, config: RabbitConfig) -> None:
        self.broker: Broker = broker
        self.config: RabbitConfig = config

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            event: IntegrationEvent = domain_event_to_integration(event=event)
            await self.broker.publish(message=asdict(event), queue=self.config.queue)

