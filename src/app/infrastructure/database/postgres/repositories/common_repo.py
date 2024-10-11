from typing import Self
from sqlalchemy.ext.asyncio import AsyncSession


class CommonSqlaRepo:
    def __init__(self: Self, session: AsyncSession) -> None:
        self.session: AsyncSession = session