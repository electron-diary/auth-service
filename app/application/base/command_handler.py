from abc import abstractmethod
from typing import Protocol, Self


class CommandHandler[Command, Response](Protocol):
    @abstractmethod
    async def __call__(self: Self, command: Command) -> Response:
        raise NotImplementedError("method must be implemented by subclasses")
