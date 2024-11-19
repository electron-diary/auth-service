from abc import abstractmethod
from typing import Protocol, Self

from app.adapters.broker.message import Message


class KafkaBrokerInterface(Protocol):
    @abstractmethod
    def produce_messages(self: Self, topic: str, message: Message) -> None:
        raise NotImplementedError(
            "method must be implemented by subclasses",
        )

    @abstractmethod
    def consume_messages(self: Self, topic: str) -> None:
        raise NotImplementedError(
            "method must be implemented by subclasses",
        )
