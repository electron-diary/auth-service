from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.application.exceptions.uow_exceptions import UoWCommitError, UoWRollbackError
from src.app.application.interfaces.uow import UnitOfWork


class SqlaUnitOfWork(UnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    async def commit(self) -> None:
        try:
            await self.session.commit()
        except SQLAlchemyError:
            raise UoWCommitError

    async def rollback(self) -> None:
        try:
            await self.session.rollback()
        except SQLAlchemyError:
            raise UoWRollbackError