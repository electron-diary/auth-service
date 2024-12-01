from dataclasses import dataclass


@dataclass(frozen=True)
class BaseQuery:
    """
    Base class for all query objects in the system following CQRS pattern.
    Implements immutable query structure for handling read operations.

    This class serves as the foundation for all queries that represent
    requests for information from the system. Queries are immutable to
    ensure consistency during processing.

    Usage:
        - Base class for specific query implementations
        - Represents read operations in the system
        - Part of Command Query Responsibility Segregation (CQRS) pattern
        - Used for data retrieval operations

    Example query implementations:
        - GetUserByIdQuery
        - ListActiveUsersQuery
        - FindOrdersByDateQuery
        - GetAccountBalanceQuery

    Note:
        - Queries should be named to describe the information being requested
        - The frozen=True decorator ensures queries are immutable once created
        - Queries should not modify system state
        - Should return data without side effects
    """

