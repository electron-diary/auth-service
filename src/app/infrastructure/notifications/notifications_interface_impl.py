from typing import Self
from datetime import datetime

from src.app.infrastructure.notifications.notifications_interface import NotificationsInterface


class NotificationsService(NotificationsInterface):
    def __init__(self: Self) -> None:
        pass

    async def send_email_notification(self: Self) -> None:
        pass

    async def send_sms_notification(self: Self) -> None:
        pass

    async def send_push_notification(self: Self) -> None:
        pass

    async def resend_notification(self: Self) -> None:
        pass
