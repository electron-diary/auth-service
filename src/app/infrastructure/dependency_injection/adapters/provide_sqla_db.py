from typing import Self, AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession
from dishka import Provider, Scope, provide, AnyOf

from src.app.infrastructure.database.postgres.config import PostgresConfig
from src.app.infrastructure.database.postgres.main import postgres_engine, postgres_session, postgres_session_factory
from src.app.application.interfaces.uow import UnitOfWork
from src.app.infrastructure.database.postgres.uow import SqlaUnitOfWork
from src.app.infrastructure.database.postgres.repositories.common_repo import CommonSqlaRepo
from src.app.infrastructure.database.postgres.repositories.user_repo import UserRepositoryImpl
from src.app.domain.user.repositories import UserInterface


class SqlaProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_sqla_config(self: Self) -> PostgresConfig:
        return PostgresConfig
    
    @provide(scope=Scope.APP)
    def provide_engine(self: Self, config: PostgresConfig) -> AsyncEngine:
        return postgres_engine(config = config)
    
    @provide(scope=Scope.APP)
    def provide_postgres_session_factory(self: Self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return postgres_session_factory(engine = engine)
    
    @provide(scope=Scope.REQUEST)
    async def provide_postgres_session(self: Self, session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
        return await postgres_session(session_factory = session_factory)

    @provide(scope=Scope.REQUEST)
    def provide_sqla_uow(self: Self, session: async_sessionmaker[AsyncSession]) -> UnitOfWork:
        return SqlaUnitOfWork(session = session)
    
    @provide(scope=Scope.REQUEST)
    def provide_user_repository(self: Self, session: async_sessionmaker[AsyncSession]) -> AnyOf[CommonSqlaRepo, UserInterface]:
        return UserRepositoryImpl(session = session)
