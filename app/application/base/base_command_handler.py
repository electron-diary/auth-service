from typing import Protocol, Self
from abc import abstractmethod

from app.application.base.base_command import BaseCommand


class BaseCommandHandler[Request: BaseCommand, Response](Protocol):
    @abstractmethod
    async def __call__(self: Self, request: Request) -> Response:
        raise NotImplementedError(
            'method must be implemented ny subclasses'
        )