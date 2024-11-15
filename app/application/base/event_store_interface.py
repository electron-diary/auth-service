from abc import abstractmethod
from collections.abc import Sequence
from typing import Protocol, Self

from app.domain.base.base_event import BaseDomainEvent


class EventStoreInterface(Protocol):
    @abstractmethod
    async def save_event(self: Self, event: Sequence[BaseDomainEvent]) -> None:
        raise NotImplementedError(
            "Method must be implemented by subclasses",
        )
