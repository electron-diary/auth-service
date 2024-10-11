from typing import Self, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession
from dishka import Provider, Scope, provide

from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.database.postgres.main import postgres_engine, postgres_session, postgres_session_factory


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_sqla_config(self: Self) -> PostgresConfig:
        return PostgresConfig
    
    @provide(scope=Scope.APP)
    async def provide_engine(self: Self, config: PostgresConfig) -> AsyncGenerator[AsyncEngine, None]:
        return await postgres_engine(config = config)
    
    @provide(scope=Scope.APP)
    def provide_postgres_session_factory(self: Self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return postgres_session_factory(engine = engine)
    
    @provide(scope=Scope.REQUEST)
    async def provide_postgres_session(self: Self, session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
        return await postgres_session(session_factory = session_factory)