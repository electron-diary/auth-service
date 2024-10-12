from typing import Self
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class CommonSqlaRepo:
    def __init__(self: Self, session: async_sessionmaker[AsyncSession]) -> None:
        self.session: async_sessionmaker[AsyncSession] = session