from typing import Protocol, Self
from abc import abstractmethod

from app.domain.base.base_event import BaseDomainEvent

class AioKafkaInterface(Protocol):
    @abstractmethod
    async def recieve_message(self: Self) -> dict[str]:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )

    @abstractmethod
    async def send_message(self: Self, message: dict[str]) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )