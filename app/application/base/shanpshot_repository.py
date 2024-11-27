from typing import Self, Protocol
from abc import abstractmethod

from app.domain.base.domain_entity import DomainEntity
from app.domain.user.value_objects import UserId


class SnaphsotRepository(Protocol):
    @abstractmethod
    def get_snapshot(self: Self, id: UserId) -> DomainEntity:
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    def save_snapshot(self: Self, snapshot: DomainEntity) -> None:
        raise NotImplementedError("method must be implemented by subclasses")