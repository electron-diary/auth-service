from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine

from app.infrastructure.database.postgres.config import PostgresConfig


def postgres_engine(config: PostgresConfig) -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        url=config.postgres_url,
        echo=True,
        echo_pool=config.echo,
        pool_size=50
    )
    return engine


engine = AsyncEngine()