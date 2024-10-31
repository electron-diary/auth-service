from typing import AsyncGenerator
import logging
from logging import Logger
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine, async_sessionmaker

from app.infrastructure.database.postgres.config import PostgresConfig


logger: Logger = logging.getLogger(__name__)


def postgres_engine(config: PostgresConfig) -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        url=config.postgres_url,
        echo=True,
        echo_pool=config.echo,
        pool_size=50
    )
    logger.info("Postgres engine created")
    return engine


def postgres_session_factory(engine: AsyncEngine) -> AsyncSession:
    session: AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    return session




