from typing import Self

from aiokafka import AIOKafkaProducer

from app.application.base.event_bus import EventBusInterface
from app.domain.base.domain_event import DomainEvent
from app.infrastructure.event_bus.config import KafkaConfig
from app.infrastructure.event_bus.converters import domain_event_to_integration_event
from app.infrastructure.event_bus.events import IntegrationEvent
from app.infrastructure.event_bus.serializers import integration_event_to_json


class EventBusImpl(EventBusInterface):
    def __init__(self: Self, producer: AIOKafkaProducer, config: KafkaConfig) -> None:
        self.producer: AIOKafkaProducer = producer
        self.config: KafkaConfig = config

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            integration_event: IntegrationEvent = domain_event_to_integration_event(event=event)
            await self.producer.send_and_wait(
                topic=self.config.topic, value=integration_event_to_json(integration_event=integration_event),
            )
