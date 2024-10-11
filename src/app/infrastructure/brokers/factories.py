from typing import Self
import logging
from faststream.nats.annotations import NatsBroker as Broker, Client
from faststream.nats.broker import NatsBroker

from src.app.infrastructure.brokers.config import NatsConfig


class BrokerFactory:
    def __init__(self: Self, config: NatsConfig) -> None:
        self.config: NatsConfig = config

    def get_broker(self: Self) -> Broker:
        broker: Broker = NatsBroker(
            servers=[self.config.nats_uri],
            log_level=logging.INFO
        )
        return broker
