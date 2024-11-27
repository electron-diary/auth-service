from dataclasses import asdict
from typing import Self

from faststream.rabbit.annotations import RabbitBroker as Broker

from app.application.base.event_queue import EventBusRepository
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored
from app.infrastructure.events.converters import domain_event_to_integration
from app.infrastructure.events.integration_event import IntegrationEvent
from app.infrastructure.message_broker.config import RabbitConfig


class EventBusImpl(EventBusRepository):
    def __init__(self: Self, broker: Broker, config: RabbitConfig) -> None:
        self.broker: Broker = broker
        self.config: RabbitConfig = config

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            integration_event: IntegrationEvent = domain_event_to_integration(event=event)
            match event:
                case UserCreated():
                    await self.broker.publish(message=asdict(integration_event), queue='user-created')
                case UserDeleted():
                    await self.broker.publish(message=asdict(integration_event), queue='user-deleted')
                case UsernameUpdated():
                    await self.broker.publish(message=asdict(integration_event), queue='username-updated')
                case UserRestored():
                    await self.broker.publish(message=asdict(integration_event), queue='user-restored')
                case ContactsUpdated():
                    await self.broker.publish(message=asdict(integration_event), queue='contacts-updated')
            

