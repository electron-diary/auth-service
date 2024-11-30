from typing import Self

from faststream.kafka.annotations import KafkaBroker

from app.application.base.event_bus import EventBusInterface
from app.domain.base.domain_event import DomainEvent
from app.infrastructure.event_bus.config import KafkaConfig
from app.infrastructure.event_bus.converters import domain_event_to_integration_event
from app.infrastructure.event_bus.events import IntegrationEvent


class EventBusImpl(EventBusInterface):
    def __init__(self: Self, producer: KafkaBroker, config: KafkaConfig) -> None:
        self.producer: KafkaBroker = producer
        self.config: KafkaConfig = config

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            integration_event: IntegrationEvent = domain_event_to_integration_event(event=event)
            await self.producer.publish(
                topic=self.config.topic, message=integration_event,
            )
