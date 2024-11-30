from typing import Self

from faststream.rabbit.annotations import RabbitBroker as RabbitBrokerAnnotation

from app.application.base.event_bus import LocalEventBusInterface
from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored


class LocalEventBusImpl(LocalEventBusInterface):
    def __init__(self: Self, broker: RabbitBrokerAnnotation) -> None:
        self.broker: RabbitBrokerAnnotation = broker

    async def publish(self: Self, events: list[DomainEvent]) -> None:
        for event in events:
            match event:
                case UserCreated():
                    await self.broker.publish(event, queue="user-created")
                case UserDeleted():
                    await self.broker.publish(event, queue="user-deleted")
                case UsernameUpdated():
                    await self.broker.publish(event, queue="username-updated")
                case UserRestored():
                    await self.broker.publish(event, queue="user-restored")
                case ContactsUpdated():
                    await self.broker.publish(event, queue="contacts-updated")
                case _:
                    raise NotImplementedError
