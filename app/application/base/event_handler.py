from abc import abstractmethod
from typing import Protocol, Self

from app.domain.base.domain_event import DomainEvent


class EventHandler[Event: DomainEvent](Protocol):
    @abstractmethod
    async def __call__(self: Self, event: Event) -> None:
        raise NotImplementedError("method must be implemented by subclasses")
