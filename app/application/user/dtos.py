from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class UserDTO:
    """
    Data Transfer Object (DTO) representing user information.
    Provides a lightweight, immutable container for transferring user data
    across application boundaries.

    Attributes:
        user_id (UUID): Unique identifier for the user
        phone_number (int): User's contact phone number
        is_deleted (bool): Flag indicating if the user account is deleted
        username (str): User's chosen display name

    Usage:
        - Transferring user data between application layers
        - Presenting user information to external interfaces
        - Response object for user queries
        - Input/Output data structure for API endpoints

    Example:
        user_dto = UserDTO(
            user_id=UUID('123e4567-e89b-12d3-a456-426614174000'),
            phone_number=1234567890,
            is_deleted=False,
            username="john_doe"
        )

    Note:
        - Immutable (frozen=True) to prevent accidental modifications
        - Contains only data, no behavior
        - Used for data transfer, not domain logic
        - Separates domain model from external representation
    """

    user_id: UUID
    phone_number: int
    is_deleted: bool
    username: str
