from typing import Self
from uuid import UUID, uuid4

from app.application.base.base_mediator import MediatorInterface
from app.application.base.command_handler import CommandHandler
from app.application.user.commands import DeleteUserCommand
from app.application.user.exceptions import  UserNotFoundError
from app.application.user.interfaces import UserWriterGatewayInterface
from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User
from app.domain.user.value_objects import  UserId


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
