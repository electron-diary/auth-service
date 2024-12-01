from dataclasses import dataclass

from app.application.base.exception import ApplicationError


@dataclass
class UserNotFoundError(ApplicationError):
    """
    Application error raised when a requested user cannot be found.
    Extends ApplicationError to handle user lookup failures.

    Usage:
        - Raised during user retrieval operations
        - Indicates invalid user references
        - Signals non-existent user access attempts

    Example scenarios:
        - User ID doesn't exist in the system
        - Attempting to update a deleted user
        - Looking up invalid username

    Example:
        raise UserNotFoundError("User with ID 123 not found")
        raise UserNotFoundError("Username 'john_doe' does not exist")
    """



@dataclass
class UserAlreadyExistsError(ApplicationError):
    """
    Application error raised when attempting to create a user that already exists.
    Extends ApplicationError to handle user creation conflicts.

    Usage:
        - Raised during user registration
        - Prevents duplicate user creation
        - Maintains user uniqueness constraints

    Example scenarios:
        - Username already taken
        - Phone number already registered
        - Attempting to restore an active user

    Example:
        raise UserAlreadyExistsError("Username 'john_doe' is already taken")
        raise UserAlreadyExistsError("Phone number already registered")
    """

