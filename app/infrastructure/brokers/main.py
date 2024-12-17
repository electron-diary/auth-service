import nats
from nats.aio.client import Client
from nats.js import JetStreamContext

from app.infrastructure.brokers.config import NatsConfig


async def get_nats_client(config: NatsConfig) -> Client:
    return await nats.connect(config.connection_link)

def get_nats_jetstream(nats_client: Client) -> JetStreamContext:
    return nats_client.jetstream()
