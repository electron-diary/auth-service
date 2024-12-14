from abc import abstractmethod
from typing import Protocol, Self

from app.domain.domain_event import DomainEvent


class EventBus(Protocol):
    @abstractmethod
    async def publish(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
