from abc import abstractmethod
from typing import Protocol, Self

from app.application.base.base_query import BaseQuery


class BaseQueryHandler[Request: BaseQuery, Response](Protocol):
    @abstractmethod
    async def __call__(self: Self, requst: Request) -> Response:
        raise NotImplementedError(
            "method must be implemented ny subclasses",
        )
