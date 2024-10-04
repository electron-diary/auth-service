from typing import Self
from datetime import datetime
from faststream.nats import NatsBroker

from src.app.infrastructure.notifications.notifications_interface import NotificationsInterface
from src.app.infrastructure.brokers import nats_broker


class NotificationsService(NotificationsInterface):
    def __init__(self: Self, broker: NatsBroker) -> None:
        self.broker: NatsBroker = broker
        
    async def send_email_notification(self: Self) -> None:
        async with self.broker as broker:
            await broker.publish(
                message='email-message',
                stream='/email-strem',
            )

    async def send_sms_notification(self: Self) -> None:
        async with self.broker as broker:
            await broker.publish(
                message='sms-message',
                stream='/sms-stream',
            )

    async def send_push_notification(self: Self) -> None:
        async with self.broker as broker:
            await broker.publish(
                message='push-message',
                stream='/push-stream',
            )

    async def resend_notification(self: Self) -> None:
        async with self.broker as broker:
            await broker.publish(
                message='resend-message',
                stream='/resend-stream',
            )
