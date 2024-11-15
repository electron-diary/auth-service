from typing import Protocol, Self, Sequence
from abc import abstractmethod

from app.domain.common.common_event import CommonDomainEvent

class EventPublisherInterface(Protocol):
    @abstractmethod
    async def apply(self: Self, event: Sequence[CommonDomainEvent]) -> None:
        raise NotImplementedError(
            'Method must be implemented by subclasses'
        )