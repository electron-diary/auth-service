from dataclasses import asdict

from nats.js.client import JetStreamContext

from app.infrastructure.brokers.interfaces import MessagePublisher
from app.infrastructure.brokers.message import Message
from app.infrastructure.common.serializers import to_json


class MessagePublisherImpl(MessagePublisher):
    def __init__(
        self,
        jetstream: JetStreamContext,
    ) -> None:
        self.jetstream = jetstream

    async def publish(self, message: Message, key: str) -> None:
        nats_message = to_json(asdict(message))
        await self.jetstream.publish(key, nats_message)
