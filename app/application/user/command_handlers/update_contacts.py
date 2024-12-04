from typing import Self

from app.application.base.base_mediator import MediatorInterface
from app.application.base.command_handler import CommandHandler
from app.application.user.commands import UpdateContactsCommand
from app.application.user.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.application.user.interfaces import UserWriterGatewayInterface
from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, UserId


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


