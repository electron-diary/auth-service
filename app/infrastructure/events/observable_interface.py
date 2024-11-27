from abc import abstractmethod
from typing import Protocol, Self

from app.application.base.event_handlers import DomainEventHandler
from app.domain.base.domain_event import DomainEvent

'''
И ЗДЕСЬ ХУИТА
'''

class ObservableInterface(Protocol):
    @abstractmethod
    def add_event_handler(self: Self, event: DomainEvent, handler: DomainEventHandler[DomainEvent]) -> None:
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def notify_observers(self: Self, event: DomainEvent) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
