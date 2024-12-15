from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from app.infrastructure.database.postgres.config import PostgresConfig


def postgres_engine(config: PostgresConfig) -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        url=config.connection_link,
        echo=True,
        echo_pool=config.echo,
        pool_size=50,
    )
    return engine
