from typing import Self
from dishka import Provider, Scope, provide
from faststream.nats.annotations import NatsBroker

from src.app.infrastructure.brokers.config import NatsConfig
from src.app.infrastructure.brokers.factories import BrokerFactory

class NatsProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_nats_config(self: Self) -> NatsConfig:
        return NatsConfig

    @provide(scope=Scope.APP)
    def provide_nats_broker(self: Self, config: NatsConfig) -> NatsBroker:
        factory: BrokerFactory = BrokerFactory(config = config)
        broker: NatsBroker = factory.get_broker()
        return broker

