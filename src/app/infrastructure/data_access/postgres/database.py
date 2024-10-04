from typing import AsyncGenerator, Self
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self: Self, db_uri: str) -> None: 
        self.db_uri: str = db_uri
        self.engine: AsyncEngine = create_async_engine(
            url = self.db_uri, echo = True
        )
        self.async_session: AsyncSession = async_sessionmaker(
            bind = self.engine, class_ = AsyncSession, expire_on_commit=False
        )

    @asynccontextmanager
    async def get_session(self: Self)->AsyncGenerator[AsyncSession, None]:
        session: AsyncSession = self.async_session()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


    async def init_models(self: Self) -> None:
        async with self.engine.begin() as connection:
            await connection.run_sync(Base.metadata.drop_all)
            await connection.run_sync(Base.metadata.create_all)