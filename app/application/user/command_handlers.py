from typing import Self
from uuid import UUID, uuid4

from app.application.base.command_handler import CommandHandler
from app.application.base.event_bus import EventBusInterface
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
    def __init__(
        self: Self, user_writer_gateway: UserWriterGatewayInterface, event_bus: EventBusInterface,
    ) -> None:
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.event_bus: EventBusInterface = event_bus

    async def __call__(self: Self, command: CreateUserCommand) -> UUID:
        if await self.user_writer_gateway.check_phone_exist(phone_number=Contacts(phone=command.phone_number)):
            raise UserAlreadyExistsError("User already exists")
        user_id: UUID = uuid4()
        user: User = User.create_user(
            id=UserId(value=user_id),
            username=Username(value=command.username),
            contacts=Contacts(phone=command.phone_number),
            is_deleted=DeletedUser(value=False),
        )
        events: list[DomainEvent] = user.get_events()

        await self.user_writer_gateway.create_user(user=user)
        await self.event_bus.publish(events=events)

        return user_id


class UpdateUsernameCommandHandler(CommandHandler[UpdateUsernameCommand, None]):
    def __init__(
        self: Self, user_writer_gateway: UserWriterGatewayInterface, event_bus: EventBusInterface,
    ) -> None:
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.event_bus: EventBusInterface = event_bus

    async def __call__(self: Self, command: UpdateUsernameCommand) -> None:
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")
        user.update_username(username=Username(value=command.username))
        events: list[DomainEvent] = user.get_events()

        if not await self.user_writer_gateway.update_user(user=user):
            raise UserAlreadyExistsError("User already exists")
        await self.event_bus.publish(events=events)


class UpdateContactsCommandHandler(CommandHandler[UpdateContactsCommand, None]):
    def __init__(
        self: Self, user_writer_gateway: UserWriterGatewayInterface, event_bus: EventBusInterface,
    ) -> None:
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.event_bus: EventBusInterface = event_bus

    async def __call__(self: Self, command: UpdateContactsCommand) -> None:
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")
        if await self.user_writer_gateway.check_phone_exist(phone_number=Contacts(phone=command.phone_number)):
            raise UserAlreadyExistsError("User already exists")
        user.update_contact(contacts=Contacts(phone=command.phone_number))
        events: list[DomainEvent] = user.get_events()

        if not await self.user_writer_gateway.update_user(user=user):
            raise UserAlreadyExistsError("User already exists")
        await self.event_bus.publish(events=events)


class DeleteUserCommandHandler(CommandHandler[DeleteUserCommand, None]):
    def __init__(
        self: Self, user_writer_gateway: UserWriterGatewayInterface, event_bus: EventBusInterface,
    ) -> None:
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.event_bus: EventBusInterface = event_bus

    async def __call__(self: Self, command: DeleteUserCommand) -> None:
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")
        user.delete_user()
        events: list[DomainEvent] = user.get_events()

        await self.user_writer_gateway.update_user(user=user)
        await self.event_bus.publish(events=events)


class RestoreUserCommandHandler(CommandHandler[RestoreUserCommand, None]):
    def __init__(
        self: Self, user_writer_gateway: UserWriterGatewayInterface, event_bus: EventBusInterface,
    ) -> None:
        self.user_writer_gateway: UserWriterGatewayInterface = user_writer_gateway
        self.event_bus: EventBusInterface = event_bus

    async def __call__(self: Self, command: RestoreUserCommand) -> None:
        user: User | None = await self.user_writer_gateway.get_user_by_id(user_id=UserId(command.user_id))
        if not user:
            raise UserNotFoundError(f"User with id {command.user_id} not found")
        user.restore_user()
        events: list[DomainEvent] = user.get_events()

        await self.user_writer_gateway.update_user(user=user)
        await self.event_bus.publish(events=events)


