from typing import Self

from app.application.base.base_query_handler import BaseQueryHandler
from app.application.interfaces.user_queries_repository import SearchUserQueriesRepository
from app.application.dto.user_dto import UserDto
from app.application.queries.search_user_by_name_query import SearchUserByNameQuery


class SearchUserByNameQueryHandler(BaseQueryHandler[SearchUserByNameQuery, UserDto]):
    def __init__(self: Self, search_user_queries_repository: SearchUserQueriesRepository) -> None:
        self.searc_user_queries_repository: SearchUserQueriesRepository = search_user_queries_repository

    async def __call__(self: Self, request: SearchUserByNameQuery) -> None:
        ...