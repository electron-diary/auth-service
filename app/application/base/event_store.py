from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.domain.base.domain_entity import DomainEntity
from app.domain.base.domain_event import DomainEvent
from app.domain.user.value_objects import UserId


class EventStoreRepository(Protocol):
    @abstractmethod
    async def save_event(self: Self, events: list[DomainEvent]) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

    @abstractmethod
    async def get_current_state(self: Self, id: UUID) -> DomainEntity:
        raise NotImplementedError("method must be implemnted by subclasses")
