from typing import Self

from app.application.user.dto import UserDTO
from app.application.user.repositories import UserReaderRepository
from app.application.user.queries import GetUserByIdQuery
from app.application.base.query_handler import QueryHandler


class GetUserByIdQueryHandler(QueryHandler[GetUserByIdQuery, UserDTO]):
    def __init__(self: Self, user_reader_repository: UserReaderRepository) -> None:
        self.user_reader_repository: UserReaderRepository = user_reader_repository

    async def __call__(self: Self, query: GetUserByIdQuery) -> UserDTO:
        return await self.user_reader_repository.get_user_by_id(user_id=query.id)