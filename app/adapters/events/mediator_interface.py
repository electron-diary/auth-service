from typing import Self, Protocol
from abc import abstractmethod

from app.domain.base.domain_event import DomainEvent
from app.application.base.event_handlers import DomainEventHandler


class MediatorInterfcae(Protocol):
    @abstractmethod
    def register_event_handler(self: Self, event: DomainEvent, handler: DomainEventHandler) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
    
    @abstractmethod
    async def send(self: Self, event: DomainEvent) -> None:
        raise NotImplementedError("method must be implemented by subclasses")