from abc import abstractmethod
from typing import Protocol, Self


class QueryHandler[Query, Response](Protocol):
    """
    Generic Protocol defining the interface for query handlers in the system.
    Implements the Query handling aspect of CQRS architecture.

    Type Parameters:
        Query: The type of query this handler processes
        Response: The type of data returned by the query

    This Protocol defines the contract that all query handlers must follow,
    ensuring consistent query handling across the application.

    Usage:
        - Define specific query handlers
        - Process read operations
        - Retrieve data from the system
        - Return query results

    Example implementations:
        class GetUserByIdHandler(QueryHandler[GetUserByIdQuery, User]):
            async def __call__(self, query: GetUserByIdQuery) -> User:
                # Implementation

        class ListActiveUsersHandler(QueryHandler[ListActiveUsersQuery, list[User]]):
            async def __call__(self, query: ListActiveUsersQuery) -> list[User]:
                # Implementation

    Note:
        - Handlers should be stateless
        - Each handler processes one specific query type
        - Handlers should not modify system state
        - Async implementation allows for I/O operations
    """

    @abstractmethod
    async def __call__(self: Self, query: Query) -> Response:
        """
        Process the given query and return requested data.

        Args:
            query (Query): The query to be processed

        Returns:
            Response: The requested data

        Raises:
            NotImplementedError: When the handler is not properly implemented
            Various application errors based on query processing
        """
        raise NotImplementedError("method must be implemented by subclasses")
