from abc import abstractmethod
from typing import Protocol, Self
from uuid import UUID

from app.application.user.dtos import UserDTO
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, UserId


class UserWriterGatewayInterface(Protocol):
    """
    Protocol defining the interface for write operations on user data.
    Implements the Gateway pattern for user persistence operations.

    This interface separates the domain model from the persistence layer,
    following the CQRS pattern for write operations.

    Usage:
        - Implement in infrastructure layer
        - Handle user persistence
        - Manage user state changes
        - Validate user constraints
    """

    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UserId) -> User | None:
        """
        Retrieves a user entity by its ID for write operations.

        Args:
            user_id (UserId): The unique identifier of the user

        Returns:
            User | None: The user entity if found, None otherwise
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def create_user(self: Self, user: User) -> None:
        """
        Persists a new user entity to the storage.

        Args:
            user (User): The user entity to be created
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def update_user(self: Self, user: User) -> None:
        """
        Updates an existing user entity in storage.

        Args:
            user (User): The user entity with updated information
        """
        raise NotImplementedError("method must be implemented by subclasses")

    @abstractmethod
    async def check_phone_exist(self: Self, phone_number: Contacts) -> User | None:
        """
        Checks if a phone number is already registered to a user.

        Args:
            phone_number (Contacts): The phone number to check

        Returns:
            User | None: The user with the phone number if exists, None otherwise
        """
        raise NotImplementedError("method must be implemented by subclasses")


class UserReaderGatewayInterface(Protocol):
    """
    Protocol defining the interface for read operations on user data.
    Implements the Gateway pattern for user query operations.

    This interface supports the read side of CQRS pattern,
    providing optimized data access for queries.

    Usage:
        - Implement in infrastructure layer
        - Handle user queries
        - Return DTOs for read operations
        - Optimize read performance
    """

    @abstractmethod
    async def get_user_by_id(self: Self, user_id: UUID) -> UserDTO | None:
        """
        Retrieves user data by ID for read operations.

        Args:
            user_id (UUID): The unique identifier of the user

        Returns:
            UserDTO | None: Data transfer object with user information if found,
                          None otherwise
        """
        raise NotImplementedError("method must be implemented by subclasses")

