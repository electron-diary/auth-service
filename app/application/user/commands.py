from dataclasses import dataclass
from uuid import UUID

from app.application.base.base_command import BaseCommand


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    """
    Command for creating a new user in the system.
    Represents the intention to register a new user with basic information.

    Attributes:
        username (str): The desired username for the new user
        phone_number (int): The user's phone number for contact information

    Usage:
        Used when registering new users in the system
        Triggers user creation process in the domain
    """

    username: str
    phone_number: int


@dataclass(frozen=True)
class UpdateContactsCommand(BaseCommand):
    """
    Command for updating a user's contact information.
    Allows modification of user's phone number while maintaining user identity.

    Attributes:
        user_id (UUID): Unique identifier of the user to update
        phone_number (int): The new phone number to be associated with the user

    Usage:
        Used when users need to update their contact information
        Ensures user contact details remain current
    """

    user_id: UUID
    phone_number: int


@dataclass(frozen=True)
class UpdateUsernameCommand(BaseCommand):
    """
    Command for changing a user's username.
    Enables users to modify their display name in the system.

    Attributes:
        user_id (UUID): Unique identifier of the user to update
        username (str): The new username to be assigned

    Usage:
        Used when users want to change their username
        Maintains user identity while updating display information
    """

    user_id: UUID
    username: str


@dataclass(frozen=True)
class DeleteUserCommand(BaseCommand):
    """
    Command for marking a user as deleted in the system.
    Implements soft delete functionality for user management.

    Attributes:
        user_id (UUID): Unique identifier of the user to delete

    Usage:
        Used when users request account deletion
        Preserves user data while removing active access
    """

    user_id: UUID


@dataclass(frozen=True)
class RestoreUserCommand(BaseCommand):
    """
    Command for restoring a previously deleted user.
    Enables reactivation of soft-deleted user accounts.

    Attributes:
        user_id (UUID): Unique identifier of the user to restore

    Usage:
        Used when previously deleted users need to be reactivated
        Restores access to existing user data
    """

    user_id: UUID
