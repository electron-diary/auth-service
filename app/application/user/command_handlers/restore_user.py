from typing import Self

from app.application.base.base_mediator import MediatorInterface
from app.application.base.command_handler import CommandHandler
from app.application.user.commands import RestoreUserCommand
from app.application.user.exceptions import UserNotFoundError
from app.application.user.interfaces import UserWriterGatewayInterface
from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User
from app.domain.user.value_objects import UserId


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



