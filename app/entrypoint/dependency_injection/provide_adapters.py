from collections.abc import AsyncGenerator
from typing import Self

from dishka import Provider, Scope, provide
from faststream.kafka.annotations import KafkaBroker as FaststreamKafkaBroker
from faststream.rabbit.annotations import RabbitBroker as FaststreamRabbitBroker
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorClientSession, AsyncIOMotorCollection, AsyncIOMotorDatabase
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from app.application.base.event_bus import GlobalEventBusInterface, LocalEventBusInterface
from app.application.user.interfaces import (
    UserProjectionsGatewayInterface,
    UserReaderGatewayInterface,
    UserWriterGatewayInterface,
)
from app.infrastructure.databases.mongo.config import MongoConfig
from app.infrastructure.databases.mongo.main import get_collection, get_database, mongo_client, mongo_session
from app.infrastructure.databases.mongo.repositories import UserProjectionsGatewayImpl, UserReaderGatewayImpl
from app.infrastructure.databases.postgres.config import PostgresConfig
from app.infrastructure.databases.postgres.main import postgres_engine, postgres_session_factory
from app.infrastructure.databases.postgres.repositories import UserWriterGatewayImpl
from app.infrastructure.event_bus.broker import get_kafka_producer
from app.infrastructure.event_bus.config import KafkaConfig
from app.infrastructure.event_bus.repositories import GlobalEventBusImpl
from app.infrastructure.tasks.broker import get_rabbit_broker
from app.infrastructure.tasks.config import RabbitConfig
from app.infrastructure.tasks.repositories import LocalEventBusImpl


class SqlalchemyProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_sqla_config(self: Self) -> PostgresConfig:
        return PostgresConfig()

    @provide(scope=Scope.APP)
    def provide_engine(self: Self, config: PostgresConfig) -> AsyncEngine:
        return postgres_engine(config=config)

    @provide(scope=Scope.APP)
    def provide_postgres_session_factory(self: Self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return postgres_session_factory(engine=engine)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_postgres_session(
        self: Self, session_factory: async_sessionmaker[AsyncSession],
    ) -> AsyncGenerator[AsyncSession, None]:
        async with session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
            finally:
                await session.close()

    @provide(scope=Scope.REQUEST)
    def provide_user_writer_gateway(self: Self, session: AsyncSession) -> UserWriterGatewayInterface:
        return UserWriterGatewayImpl(session=session)


class GlobalEventBusProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_kafka_config(self: Self) -> KafkaConfig:
        return KafkaConfig()

    @provide(scope=Scope.APP)
    async def provide_kafka_producer(self: Self, config: KafkaConfig) -> FaststreamKafkaBroker:
        broker: FaststreamKafkaBroker = get_kafka_producer(config=config)
        await broker.start()
        return broker

    @provide(scope=Scope.REQUEST)
    def provide_event_bus(self: Self, producer: FaststreamKafkaBroker, config: KafkaConfig) -> GlobalEventBusInterface:
        return GlobalEventBusImpl(producer=producer, config=config)


class LocalEventBusProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_rabbit_config(self: Self) -> RabbitConfig:
        return RabbitConfig()

    @provide(scope=Scope.APP)
    async def provide_rabbit_broker(self: Self, config: RabbitConfig) -> FaststreamRabbitBroker:
        broker: FaststreamRabbitBroker = get_rabbit_broker(config=config)
        await broker.start()
        return broker

    @provide(scope=Scope.REQUEST)
    def provide_event_bus(self: Self, broker: FaststreamRabbitBroker) -> LocalEventBusInterface:
        return LocalEventBusImpl(broker=broker)


class MongodbProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_mongo_config(self: Self) -> MongoConfig:
        return MongoConfig()

    @provide(scope=Scope.APP)
    async def provide_mongo_client(self: Self, config: MongoConfig) -> AsyncIOMotorClient:
        return mongo_client(config=config)

    @provide(scope=Scope.APP)
    def provide_mongo_database(
        self: Self, config: MongoConfig, client: AsyncIOMotorClient,
    ) -> AsyncIOMotorDatabase:
        return get_database(config=config, mongo_client=client)

    @provide(scope=Scope.APP)
    def provide_mongo_collection(self: Self, database: AsyncIOMotorDatabase, config: MongoConfig) -> AsyncIOMotorCollection:
        return get_collection(database=database, config=config)

    @provide(scope=Scope.APP)
    async def provide_mongo_session(self: Self, client: AsyncIOMotorClient) -> AsyncIOMotorClientSession:
        return await mongo_session(client=client)

    @provide(scope=Scope.REQUEST)
    def provide_user_projections_gateway(
        self: Self, collection: AsyncIOMotorCollection, session: AsyncIOMotorClientSession,
    ) -> UserProjectionsGatewayInterface:
        return UserProjectionsGatewayImpl(collection=collection, session=session)

    @provide(scope=Scope.REQUEST)
    def provide_user_reader_gateway(
        self: Self, collection: AsyncIOMotorCollection, session: AsyncIOMotorClientSession,
    ) -> UserReaderGatewayInterface:
        return UserReaderGatewayImpl(collection=collection, session=session)
