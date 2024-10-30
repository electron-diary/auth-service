from typing import Self
import logging
from logging import Logger
from faststream.nats.annotations import NatsBroker as Broker, Client
from faststream.nats.broker import NatsBroker

from src.app.infrastructure.brokers.config import NatsConfig


logger: Logger = logging.getLogger(__name__)


class BrokerFactory:
    def __init__(self: Self, config: NatsConfig) -> None:
        self.config: NatsConfig = config

    def get_broker(self: Self) -> Broker:
        broker: Broker = NatsBroker(
            servers=[self.config.nats_uri],
            log_level=logging.INFO
        )
        return broker
    
class BrokerConnection:
    def __init__(self: Self, broker: Broker) -> None:
        self.broker: Broker = broker

    async def connect(self: Self) -> Client:
        logger.info(f"Broker connected to {self.config.nats_uri}")
        return await self.broker.connect()
