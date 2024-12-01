from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_query import BaseQuery


@dataclass(frozen=True)
class GetUserQuery(BaseQuery):
    """
    Query object for retrieving user information by ID.
    Implements a read operation following CQRS pattern.

    Attributes:
        user_id (UUID): The unique identifier of the user to retrieve

    Usage:
        - Request user information from the system
        - Part of read-side operations in CQRS
        - Used by query handlers to fetch user data

    Example:
        query = GetUserQuery(user_id=UUID('123e4567-e89b-12d3-a456-426614174000'))
        user_dto = await user_query_handler(query)

    Note:
        - Immutable (frozen=True) to prevent modifications after creation
        - Returns UserDTO through its handler
        - Used for read-only operations
        - Does not modify system state
    """

    user_id: UUID
