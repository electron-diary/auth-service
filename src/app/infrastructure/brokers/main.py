from collections.abc import AsyncGenerator
from faststream.nats.annotations import Client

from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.brokers.factories import ConnectionFactory


async def build_nats_connection(
    nats_config: NatsConfig
) -> AsyncGenerator[Client, None]:
    nats_connection_pool = ConnectionFactory(config=nats_config).get_connection()
    async with nats_connection_pool as nats_connection:
        yield nats_connection