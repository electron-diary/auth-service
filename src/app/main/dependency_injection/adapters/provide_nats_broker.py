from typing import Self
from dishka import Provider, Scope, provide
from faststream.nats.annotations import NatsBroker, Client

from app.infrastructure.brokers.config import NatsConfig
from app.infrastructure.brokers.factories import BrokerFactory
from app.infrastructure.brokers.factories import BrokerConnection
from app.main.config import ConfigFactory

class NatsProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_nats_config(self: Self, config: ConfigFactory) -> NatsConfig:
        return config.postgres_config

    @provide(scope=Scope.APP)
    def provide_nats_broker(self: Self, config: NatsConfig) -> NatsBroker:
        factory: BrokerFactory = BrokerFactory(config = config)
        broker: NatsBroker = factory.get_broker()
        return broker
    
    @provide(scope=Scope.APP)
    async def provide_nats_connection(self: Self, broker: NatsBroker) -> Client:
        factory: BrokerConnection = BrokerConnection(broker = broker)
        connection: Client = await factory.connect()
        return connection


