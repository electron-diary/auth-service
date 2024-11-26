from abc import abstractmethod
from typing import Protocol, Self


class CommandHandler[Command](Protocol):
    @abstractmethod
    async def __call__(self: Self, command: Command) -> None:
        raise NotImplementedError("method must be implemnted by subclasses")

