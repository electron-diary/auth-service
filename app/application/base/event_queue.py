from abc import abstractmethod
from typing import Protocol, Self

from app.domain.base.domain_event import DomainEvent


class GlobalEventBusRepository(Protocol):
    @abstractmethod
    async def publish(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")


class LocalEventBusRepository(Protocol):
    @abstractmethod
    async def publish(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")