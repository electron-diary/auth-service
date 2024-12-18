from abc import abstractmethod
from typing import Protocol

from app.domain.common.domain_event import DomainEvent


class EventBus(Protocol):
    @abstractmethod
    async def publish(self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
