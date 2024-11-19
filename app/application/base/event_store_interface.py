from abc import abstractmethod
from collections.abc import Sequence
from typing import Protocol, Self

from app.domain.base.base_event import BaseDomainEvent
from app.domain.value_objects.uuid_value_object import UUIDValueObject


class EventStoreInterface(Protocol):
    @abstractmethod
    async def save_event(self: Self, event: Sequence[BaseDomainEvent]) -> None:
        msg = "Method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    async def get_events(self: Self, uuid: UUIDValueObject) -> Sequence[BaseDomainEvent]:
        msg = "Method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
