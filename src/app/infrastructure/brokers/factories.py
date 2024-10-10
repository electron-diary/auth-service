from typing import Self
import logging
from faststream.nats.annotations import NatsBroker as Broker, Client
from faststream.nats.broker import NatsBroker

from src.app.infrastructure.brokers.config import NatsConfig


class ConnectionFactory:
    def __init__(self: Self, config: NatsConfig) -> None:
        self.config: NatsConfig = config

    async def get_connection(self: Self) -> Client:
        broker: Broker = NatsBroker(
            servers=[self.config.nats_uri()],
            log_level=logging.INFO
        )

        return await broker.connect()
