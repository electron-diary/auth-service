from typing import Self
from uuid import UUID, uuid4
from datetime import datetime

from app.application.base.command_handler import CommandHandler
from app.application.base.event_queue import EventBusRepository
from app.application.base.event_store import EventStoreRepository
from app.domain.user.builder import UserBuilder
from app.domain.user.user import User
from app.domain.base.domain_event import DomainEvent
from app.domain.user.value_objects import UserId, Username, DeleteDate, Contacts, CreatedDate
from app.application.user.commands import (
    CreateUserCommand, 
    DeleteUserCommand, 
    UpdateContactsCommand, 
    UpdateUsernameCommand, 
    RestoreUserCommand
)


class CreateUserCommandHandler(CommandHandler[CreateUserCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: CreateUserCommand) -> None:
        created_date: datetime = datetime.now()
        id: UUID = uuid4()
        user: User = UserBuilder.create_user(
            id=id,
            username=Username(command.username),
            contacts=Contacts(email=command.email, phone=command.phone_number),
            delete_date=DeleteDate(None),
            created_date=CreatedDate(created_date),
        )
        events: list[DomainEvent] = ...

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class UpdateUsernameCommandHandler(CommandHandler[UpdateUsernameCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: UpdateUsernameCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.id)
        user.update_username(username=Username(command.username))
        events: list[DomainEvent] = ...

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class UpdateContactsCommandHandler(CommandHandler[UpdateContactsCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: UpdateContactsCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.id)
        user.update_contacts(contacts=Contacts(email=command.email, phone=command.phone_number))
        events: list[DomainEvent] = ...

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class DeleteUserCommandHandler(CommandHandler[DeleteUserCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: DeleteUserCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.id)
        user.delete(delete_date=DeleteDate(datetime.now()))
        events: list[DomainEvent] = ...

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)


class RestoreUserCommandHandler(CommandHandler[RestoreUserCommand]):
    def __init__(self: Self, event_store: EventStoreRepository, event_bus: EventBusRepository) -> None:
        self.event_store: EventStoreRepository = event_store
        self.event_bus: EventBusRepository = event_bus

    async def __call__(self: Self, command: RestoreUserCommand) -> None:
        user: User = await self.event_store.get_current_state(id=command.id)
        user.restore()
        events: list[DomainEvent] = ...

        await self.event_store.save_event(events=events)
        await self.event_bus.publish(events=events)