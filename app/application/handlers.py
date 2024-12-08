from typing import Self, Protocol
from abc import abstractmethod


class CommandHandler[Command, Response](Protocol):
    @abstractmethod
    def handle(self: Self, command: Command) -> Response:
        raise NotImplementedError("Method must be implemented by subclasses")
    

class QueryHandler[Query, Response](Protocol):
    @abstractmethod
    def handle(self: Self, query: Query) -> Response:
        raise NotImplementedError("Method must be implemented by subclasses")