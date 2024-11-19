from abc import abstractmethod
from typing import Protocol, Self


class AioKafkaInterface(Protocol):
    @abstractmethod
    async def recieve_message(self: Self) -> dict[str]:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )

    @abstractmethod
    async def send_message(self: Self, message: dict[str]) -> None:
        msg = "method must be implemented by subclasses"
        raise NotImplementedError(
            msg,
        )
