from abc import abstractmethod
from typing import Protocol, Self


class QueryHandler[Query, Response](Protocol):
    @abstractmethod
    async def __call__(self: Self, query: Query) -> Response:
        raise NotImplementedError("method must be implemented by subclasses")
