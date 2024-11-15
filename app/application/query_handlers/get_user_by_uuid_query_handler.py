from typing import Self

from app.application.base.base_query_handler import BaseQueryHandler
from app.application.dto.user_dto import UserDto
from app.application.interfaces.user_queries_repository import UserQueriesRepository
from app.application.queries.get_user_by_uuid_query import GetUserByUUIDQuery


class GetUserByUUIDQueryHandler(BaseQueryHandler[GetUserByUUIDQuery, UserDto]):
    def __init__(self: Self, user_queries_repository: UserQueriesRepository) -> None:
        self.user_queries_repository: UserQueriesRepository = user_queries_repository

    async def __call__(self: Self, request: GetUserByUUIDQuery) -> None:
        user: UserDto = await self.user_queries_repository.get_user_by_id(request.uuid)

        return user
