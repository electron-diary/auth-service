from abc import abstractmethod
from typing import Protocol, Self

from app.domain.base.domain_event import DomainEvent


class DomainEventHandler[event: DomainEvent](Protocol):
    @abstractmethod
    async def __call__(self: Self, event: event) -> None:
        raise NotImplementedError("method must be implemented by subclasess")
