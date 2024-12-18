from abc import abstractmethod
from typing import Protocol

from app.infrastructure.brokers.message import Message


class MessagePublisher(Protocol):
    @abstractmethod
    async def publish(self, message: Message, key: str) -> None:
        raise NotImplementedError("Method must be implemented by subclasses")
