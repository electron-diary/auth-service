from typing import Self
from uuid import UUID, uuid4

from app.application.base.base_mediator import MediatorInterface
from app.application.base.command_handler import CommandHandler
from app.application.user.commands import (
    CreateUserCommand,
    DeleteUserCommand,
    RestoreUserCommand,
    UpdateContactsCommand,
    UpdateUsernameCommand,
)
from app.application.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.application.user.interfaces import UserWriterGatewayInterface
from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


class CreateUserCommandHandler(CommandHandler[CreateUserCommand, UUID]):
    """Handles user creation commands. Returns new user UUID."""

    def __init__(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        mediator_interface: MediatorInterface,
    ) -> None:
        """Initialize with required gateways."""
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.mediator_interface: MediatorInterface = mediator_interface

    async def __call__(self: Self, command: CreateUserCommand) -> UUID:
        """
        Create new user if phone number doesn't exist.
        Returns: UUID of created user
        Raises: UserAlreadyExistsError if phone number exists
        """
        # Check if phone number already exists
        if await self.user_writer_gateway.check_phone_exist(phone_number=Contacts(phone=command.phone_number)):
            raise UserAlreadyExistsError("User already exists")

        # Generate new user ID and create user entity
        user_id: UUID = uuid4()
        user: User = User.create_user(
            id=UserId(value=user_id),
            username=Username(value=command.username),
            contacts=Contacts(phone=command.phone_number),
            is_deleted=DeletedUser(value=False),
        )
        events: list[DomainEvent] = user.get_events()

        # Persist user and process domain events
        await self.user_writer_gateway.create_user(user=user)
        await self.mediator_interface.process_events(events=events)

        return user_id


class UpdateUsernameCommandHandler(CommandHandler[UpdateUsernameCommand, None]):
    """Handles username update commands."""

    def __init__(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        mediator_interface: MediatorInterface,
    ) -> None:
        """Initialize with required gateways."""
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.mediator_interface: MediatorInterface = mediator_interface

    async def __call__(self: Self, command: UpdateUsernameCommand) -> None:
        """
        Update username for existing user.
        Raises: UserNotFoundError if user doesn't exist
        """
        # Fetch and validate user existence
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")

        # Update username and collect events
        user.update_username(username=Username(value=command.username))
        events: list[DomainEvent] = user.get_events()

        # Persist changes and process events
        await self.user_writer_gateway.create_user(user=user)
        await self.mediator_interface.process_events(events=events)


class UpdateContactsCommandHandler(CommandHandler[UpdateContactsCommand, None]):
    """Handles contact information update commands."""

    def __init__(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        mediator_interface: MediatorInterface,
    ) -> None:
        """Initialize with required gateways."""
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.mediator_interface: MediatorInterface = mediator_interface

    async def __call__(self: Self, command: UpdateContactsCommand) -> None:
        """
        Update user's contact information if phone number is unique.
        Raises: 
            - UserNotFoundError if user doesn't exist
            - UserAlreadyExistsError if phone number is taken
        """
        # Fetch and validate user existence
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")

        # Check if phone number is available
        if await self.user_writer_gateway.check_phone_exist(phone_number=Contacts(phone=command.phone_number)):
            raise UserAlreadyExistsError("User already exists")

        # Update contacts and collect events
        user.update_contact(contacts=Contacts(phone=command.phone_number))
        events: list[DomainEvent] = user.get_events()

        # Persist changes and process events
        await self.user_writer_gateway.create_user(user=user)
        await self.mediator_interface.process_events(events=events)


class DeleteUserCommandHandler(CommandHandler[DeleteUserCommand, None]):
    """Handles user deletion commands (soft delete)."""

    def __init__(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        mediator_interface: MediatorInterface,
    ) -> None:
        """Initialize with required gateways."""
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.mediator_interface: MediatorInterface = mediator_interface

    async def __call__(self: Self, command: DeleteUserCommand) -> None:
        """
        Mark user as deleted in the system.
        Raises: UserNotFoundError if user doesn't exist
        """
        # Fetch and validate user existence
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")

        # Mark user as deleted and collect events
        user.delete_user()
        events: list[DomainEvent] = user.get_events()

        # Persist changes and process events
        await self.user_writer_gateway.create_user(user=user)
        await self.mediator_interface.process_events(events=events)


class RestoreUserCommandHandler(CommandHandler[RestoreUserCommand, None]):
    """Handles user restoration commands."""

    def __init__(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        mediator_interface: MediatorInterface,
    ) -> None:
        """Initialize with required gateways."""
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.mediator_interface: MediatorInterface = mediator_interface

    async def __call__(self: Self, command: RestoreUserCommand) -> None:
        """
        Restore a previously deleted user.
        Raises: UserNotFoundError if user doesn't exist
        """
        # Fetch and validate user existence
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")

        # Restore user and collect events
        user.recovery_user()
        events: list[DomainEvent] = user.get_events()

        # Persist changes and process events
        await self.user_writer_gateway.create_user(user=user)
        await self.mediator_interface.process_events(events=events)



