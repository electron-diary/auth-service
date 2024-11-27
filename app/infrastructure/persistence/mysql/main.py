from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.infrastructure.persistence.mysql.config import MySqlConfig


def mysql_engine(config: MySqlConfig) -> AsyncEngine:
    engine: AsyncEngine = create_async_engine(
        url=config.get_connection_url,
        echo=True,
        pool_size=50,
    )
    return engine


def mysql_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session: AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
    return session