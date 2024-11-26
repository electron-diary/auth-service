from typing import Self
from dataclasses import dataclass

from app.adapters.events.mediator_interface import MediatorInterfcae
from app.domain.base.domain_event import DomainEvent
from app.application.base.event_handlers import DomainEventHandler


@dataclass(frozen=True)
class EventListener:
    event: DomainEvent
    event_handler: DomainEventHandler


class MediatorImpl(MediatorInterfcae):
    def __init__(self: Self) -> None:
        self.listeners: list[EventListener] = []

    def register_event_handler(self: Self, event: DomainEvent, handler: DomainEventHandler):
        event_listener: EventListener = EventListener(event=event, event_handler=handler)
        self.listeners.append(event_listener)

    async def publish(self: Self, event: DomainEvent):
        for listener in self.listeners:
            if isinstance(event, listener.event):
                await listener.event_handler(event)