from typing import AsyncGenerator
import json
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, AsyncEngine, async_sessionmaker

from src.app.infrastructure.database.postgres.config import PostgresConfig


def postgres_engine(config: PostgresConfig) -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        url=config.postgres_url,
        echo=True,
        future=True,
        echo_pool=config.echo,
        json_serializer=lambda obj: json.dumps(obj, ensure_ascii=False),
        json_deserializer=lambda json_str: json.loads(json_str, strict=False),
        pool_size=50
    )
    return engine


def postgres_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session: AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    return session


async def postgres_session(session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session


