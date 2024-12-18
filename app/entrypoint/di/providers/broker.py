from dishka import Provider, Scope, provide

from app.application.common.event_bus import EventBus
from app.infrastructure.brokers.config import NatsConfig
from app.infrastructure.brokers.interfaces import MessagePublisher
from app.infrastructure.brokers.message_publisher import MessagePublisherMock
from app.infrastructure.event_queue.event_bus import EventBusImpl


class NatsBrokerProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_nats_config(self) -> NatsConfig:
        return NatsConfig()

    # @provide(scope=Scope.APP)
    # async def provide_nats_client(
    #     self,
    #     config: NatsConfig,
    # ) -> Client:
    #     return await get_nats_client(config)

    # @provide(scope=Scope.APP)
    # def provide_nats_jetstream(
    #     self,
    #     client: Client,
    # ) -> JetStreamContext:
    #     return get_nats_jetstream(client)

    @provide(scope=Scope.REQUEST)
    def provide_message_publisher(
        self,
    ) -> MessagePublisher:
        return MessagePublisherMock()

    @provide(scope=Scope.REQUEST)
    def provide_event_bus(
        self,
        message_publisher: MessagePublisher,
    ) -> EventBus:
        return EventBusImpl(message_publisher)
