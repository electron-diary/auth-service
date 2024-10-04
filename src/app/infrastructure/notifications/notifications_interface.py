from typing import Protocol, Self
from abc import abstractmethod


class NotificationsInterface(Protocol):
    @abstractmethod
    async def send_sms_notification(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def send_email_notification(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def send_push_notification(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )
    
    @abstractmethod
    async def resend_notification(self: Self) -> None:
        raise NotImplementedError(
            'method must be implemented by subclasses'
        )