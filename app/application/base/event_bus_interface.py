from typing import Protocol, Self, Sequence
from abc import abstractmethod

from app.domain.common.common_event import CommonDomainEvent


class EventBusInterface(Protocol):
    @abstractmethod
    async def send_event(self: Self, event: Sequence[CommonDomainEvent]) -> None:
        raise NotImplementedError(
            'Method must be implemented by subclasses'
        )