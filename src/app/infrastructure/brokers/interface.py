from typing import Self, Protocol
from abc import abstractmethod

from app.infrastructure.brokers.message import Message


class BrokerInterface(Protocol):
    @abstractmethod
    async def publish_message(
        self: Self, message: Message, publish_to: str
    ) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def consume_message(
        self: Self, message: Message, 
    ) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )