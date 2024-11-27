from collections.abc import AsyncGenerator
from typing import Self

from dishka import Provider, Scope, provide
from faststream.rabbit.annotations import RabbitBroker
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker

from app.application.base.event_queue import GlobalEventBusRepository
from app.application.user.repositories import UserReaderRepository, UserWriterRepository
from app.infrastructure.message_broker.config import RabbitConfig
from app.infrastructure.message_broker.event_bus import GlobalEventBusImpl
from app.infrastructure.message_broker.main import get_rabbit_broker
from app.infrastructure.persistence.postgres.config import PostgresConfig
from app.infrastructure.persistence.postgres.main import postgres_engine, postgres_session_factory
from app.infrastructure.persistence.postgres.repositories import UserReaderImpl, UserWriterImpl
from app.infrastructure.message_broker.event_bus import GlobalEventBusImpl


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self: Self) -> PostgresConfig:
        return PostgresConfig()

    @provide(scope=Scope.APP)
    def provide_engine(self: Self, config: PostgresConfig) -> AsyncEngine:
        return postgres_engine(config=config)

    @provide(scope=Scope.APP)
    def provide_session_factory(self: Self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return postgres_session_factory(engine=engine)

    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_session(self: Self, session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
        async with session_factory() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
            finally:
                await session.close()

    @provide(scope=Scope.REQUEST)
    def provide_user_reader(self: Self, session: AsyncSession) -> UserReaderRepository:
        return UserReaderImpl(session=session)

    @provide(scope=Scope.REQUEST)
    def provide_user_writer(self: Self, session: AsyncSession) -> UserWriterRepository:
        return UserWriterImpl(session=session)


class RabbitProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_config(self: Self) -> RabbitConfig:
        return RabbitConfig()

    @provide(scope=Scope.APP)
    async def provide_broker(self: Self, config: RabbitConfig) -> RabbitBroker:
        broker: RabbitBroker = get_rabbit_broker(config=config)
        await broker.start() #возможно костыль
        return broker

    @provide(scope=Scope.REQUEST)
    def provide_event_bus(self: Self, broker: RabbitBroker, config: RabbitConfig) -> GlobalEventBusRepository:
        return GlobalEventBusImpl(broker=broker, config=config)
