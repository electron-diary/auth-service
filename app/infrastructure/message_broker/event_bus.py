from dataclasses import asdict
from typing import Self

from faststream.rabbit.annotations import RabbitBroker as Broker
from faststream.kafka.annotations import KafkaBroker as Kafka

from app.application.base.event_queue import EventBusRepository, LocalEventBusRepository
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored
from app.infrastructure.message_broker.converters import domain_event_to_integration
from app.infrastructure.message_broker.integration_event import IntegrationEvent
from app.infrastructure.message_broker.config import RabbitConfig
from app.infrastructure.message_broker.config import KafkaConfig


class LocalEventBusImpl(LocalEventBusRepository):
    def __init__(self: Self, broker: Broker) -> None:
        self.broker: Broker = broker

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            match event:
                case UserCreated():
                    await self.broker.publish(message=asdict(event), queue='user-created')
                case UserDeleted():
                    await self.broker.publish(message=asdict(event), queue='user-deleted')
                case UsernameUpdated():
                    await self.broker.publish(message=asdict(event), queue='username-updated')
                case UserRestored():
                    await self.broker.publish(message=asdict(event), queue='user-restored')
                case ContactsUpdated():
                    await self.broker.publish(message=asdict(event), queue='contacts-updated')

class GlobalEventBusImpl(EventBusRepository):
    def __init__(self: Self, broker: Kafka, config: KafkaConfig) -> None:
        self.broker: Kafka = broker
        self.config: KafkaConfig = config

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            integration_event: IntegrationEvent = domain_event_to_integration(event=event)
            await self.broker.publish(message=integration_event, topic=self.config.topic)
            

