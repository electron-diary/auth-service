from abc import abstractmethod
from typing import Protocol, Self

from app.adapters.broker.message import Message


class KafkaBrokerInterface(Protocol):
    @abstractmethod
    def produce_messages(self: Self, topic: str, message: Message) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    def consume_messages(self: Self, topic: str) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
