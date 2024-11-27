from dataclasses import dataclass
from typing import Self

from app.application.base.event_handlers import DomainEventHandler
from app.domain.base.domain_event import DomainEvent
from app.infrastructure.events.observable_interface import ObservableInterface

'''
ЗДЕСЬ ХУИТА
'''
@dataclass(frozen=True)
class Observer:
    event: DomainEvent
    event_handler: DomainEventHandler[DomainEvent]


class ObservableImpl(ObservableInterface):
    def __init__(self: Self) -> None:
        self.observers: list[Observer] = []

    def add_event_handler(self: Self, event: DomainEvent, handler: DomainEventHandler[DomainEvent]) -> None:
        observer: Observer = Observer(event=event, event_handler=handler)
        self.observers.append(observer)

    async def notify_observers(self: Self, event: DomainEvent) -> None:
        for observer in self.observers:
            if isinstance(event, observer.event):
                await observer.event_handler(event=event)
