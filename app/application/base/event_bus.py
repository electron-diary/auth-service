from abc import abstractmethod
from typing import Protocol, Self

from app.domain.base.domain_event import DomainEvent


class GlobalEventBusInterface(Protocol):
    @abstractmethod
    async def publish(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("method must be implemented by subclasses")


class LocalEventBusInterface(Protocol):
    @abstractmethod
    async def publish(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("method must be implemented by subclasses")