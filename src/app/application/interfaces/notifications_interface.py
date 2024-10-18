from typing import Protocol, Self
from abc import abstractmethod


class NotificationsInterface(Protocol):
    @abstractmethod
    async def send_notification_to_email(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )

    @abstractmethod
    async def send_notification_to_phone(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )