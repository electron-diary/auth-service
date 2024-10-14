from typing import Self, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession
from dishka import Provider, Scope, provide, AnyOf
import logging

from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.database.postgres.main import postgres_engine, postgres_session_factory
from src.app.infrastructure.database.postgres.repositories.common_repo import CommonSqlaRepo
from src.app.infrastructure.database.postgres.repositories.user_repo import UserRepositoryImpl
from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.main.config import ConfigFactory


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_sqla_config(self: Self, config: ConfigFactory) -> PostgresConfig:
        return config.postgres_config
    
    @provide(scope=Scope.APP)
    def provide_engine(self: Self, config: PostgresConfig) -> AsyncEngine:
        return postgres_engine(config = config)
    
    @provide(scope=Scope.APP)
    def provide_postgres_session_factory(self: Self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return postgres_session_factory(engine = engine)
    
    @provide(scope=Scope.REQUEST, provides=AsyncSession)
    async def provide_postgres_session(self: Self, session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
        async with session_factory() as session:
            try:
                yield session
                await session.commit()
                print("Session commited")
            except Exception:
                await session.rollback()
            finally:
                await session.close()
                print("Session closed")
    
    @provide(scope=Scope.REQUEST)
    def provide_user_repository(self: Self, session: AsyncSession) -> AnyOf[CommonSqlaRepo, UserRepositoryInterface]:
        return UserRepositoryImpl(session = session)


