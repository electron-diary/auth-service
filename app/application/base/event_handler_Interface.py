from abc import abstractmethod
from typing import Protocol, Self


class EventHandlerInterface(Protocol):
    @abstractmethod
    async def __call__(self: Self) -> None:
        msg = "method must be implemented ny subclasses"
        raise NotImplementedError(
            msg,
        )
