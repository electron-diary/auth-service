from typing import Self

from app.application.base.query_handler import QueryHandler
from app.application.user.dtos import UserDTO
from app.application.user.exceptions import UserNotFoundError
from app.application.user.interfaces import UserReaderGatewayInterface
from app.application.user.queries import GetUserQuery


class GetUserByIdQueryHandler(QueryHandler[GetUserQuery, UserDTO]):
    def __init__(self: Self, user_reader_gateway: UserReaderGatewayInterface) -> None:
        self.user_reader_gateway: UserReaderGatewayInterface = user_reader_gateway

    async def __call__(self: Self, query: GetUserQuery) -> UserDTO:
        user: UserDTO | None = await self.user_reader_gateway.get_user_by_id(query.user_id)
        if user is None:
            raise UserNotFoundError(f"User with id {query.user_id} not found")
        return user
