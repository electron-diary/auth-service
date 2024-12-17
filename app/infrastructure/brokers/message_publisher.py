from dataclasses import asdict
from typing import Self

from nats.js.client import JetStreamContext

from app.infrastructure.brokers.interfaces import MessagePublisher
from app.infrastructure.brokers.message import Message
from app.infrastructure.common.serializers import to_json


class MessagePublisherImpl(MessagePublisher):
    def __init__(
        self: Self,
        jetstream: JetStreamContext,
    ) -> None:
        self.jetstream = jetstream

    async def publish(self: Self, message: Message, key: str) -> None:
        nats_message = to_json(asdict(message))
        await self.jetstream.publish(key, nats_message)
