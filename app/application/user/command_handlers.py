from typing import Self
from uuid import UUID, uuid4

from app.application.base.command_handler import CommandHandler
from app.application.base.event_queue import EventBusRepository
from app.application.base.event_store import EventStoreRepository
from app.application.user.commands import (
    CreateUserCommand,
    DeleteUserCommand,
    RestoreUserCommand,
    UpdateContactsCommand,
    UpdateUsernameCommand,
)
from app.domain.base.domain_event import DomainEvent
from app.domain.user.builder import UserBuilder
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


class CreateUserCommandHandler(CommandHandler[CreateUserCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: CreateUserCommand) -> None:
        user: User = UserBuilder.create_user(
            id=UserId(command.user_id),
            username=Username(command.username),
            contacts=Contacts(email=command.email, phone=command.phone_number),
            is_deleted=DeletedUser(False),
        )
        events: list[DomainEvent] = user.get_actions()

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class UpdateUsernameCommandHandler(CommandHandler[UpdateUsernameCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: UpdateUsernameCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.user_id)
        user.update_username(username=Username(command.username))
        events: list[DomainEvent] = user.get_actions()

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class UpdateContactsCommandHandler(CommandHandler[UpdateContactsCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: UpdateContactsCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.user_id)
        user.update_contacts(contacts=Contacts(email=command.email, phone=command.phone_number))
        events: list[DomainEvent] = user.get_actions()

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class DeleteUserCommandHandler(CommandHandler[DeleteUserCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: DeleteUserCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.user_id)
        user.delete_user()
        events: list[DomainEvent] = user.get_actions()

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class RestoreUserCommandHandler(CommandHandler[RestoreUserCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: RestoreUserCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.user_id)
        user.recovery_user()
        events: list[DomainEvent] = user.get_actions()

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)
