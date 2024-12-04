from typing import Self

from app.application.base.query_handler import QueryHandler
from app.application.user.dtos import UserDTO
from app.application.user.exceptions import UserNotFoundError
from app.application.user.interfaces import UserReaderGatewayInterface
from app.application.user.queries import GetUserQuery


class GetUserByIdQueryHandler(QueryHandler[GetUserQuery, UserDTO]):
    """
    Query handler for retrieving user information by ID.
    Implements the Query Handler pattern for processing GetUserQuery requests.

    Type Parameters:
        GetUserQuery: The input query type
        UserDTO: The response type containing user information

    This handler coordinates between the application layer and the persistence layer,
    retrieving user data through the reader gateway.

    Usage:
        - Process user lookup requests
        - Return user information as DTO
        - Handle user not found scenarios
        - Part of CQRS read operations
    """

    def __init__(self: Self, user_reader_gateway: UserReaderGatewayInterface) -> None:
        """
        Initialize the query handler with required dependencies.

        Args:
            user_reader_gateway (UserReaderGatewayInterface): Gateway for reading user data
        """
        self.user_reader_gateway: UserReaderGatewayInterface = user_reader_gateway

    async def __call__(self: Self, query: GetUserQuery) -> UserDTO:
        """
        Process the get user query and return user information.

        Args:
            query (GetUserQuery): Query containing the user ID to look up

        Returns:
            UserDTO: Data transfer object containing user information

        Raises:
            UserNotFoundError: When the requested user doesn't exist

        Example:
            handler = GetUserByIdQueryHandler(user_reader_gateway)
            user_dto = await handler(GetUserQuery(user_id=uuid))
        """
        user: UserDTO | None = await self.user_reader_gateway.get_user_by_id(query.user_id)
        if user is None:
            raise UserNotFoundError(f"User with id {query.user_id} not found")
        return user
