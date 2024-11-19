from abc import abstractmethod
from typing import Protocol, Self

from app.application.base.integration_event import IntegrationEvent


class ProjectorInterface(Protocol):
    @abstractmethod
    async def project(self: Self, event: IntegrationEvent) -> None:
        msg = "method must be implemented ny subclasses"
        raise NotImplementedError(
            msg,
        )
