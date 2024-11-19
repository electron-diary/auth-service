from typing import TYPE_CHECKING, Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.event_store_interface import EventStoreInterface
from app.application.commands.delete_user_commands import DeleteUserCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.uuid_value_object import UUIDValueObject

if TYPE_CHECKING:
    from collections.abc import Sequence

    from app.domain.base.base_event import BaseDomainEvent


class DeleteUserCommandHandler(BaseCommandHandler[DeleteUserCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository,
        event_bus: EventBusInterface,
        event_store: EventStoreInterface,
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.event_bus: EventBusInterface = event_bus
        self.event_store: EventStoreInterface = event_store

    async def __call__(self: Self, request: DeleteUserCommand) -> None:
        uuid: UUIDValueObject = UUIDValueObject(request.user_uuid)
        await self.event_store.get_events(uuid=uuid)
        user: UserDomainEntity = UserDomainEntity.replay_events()

        await self.user_commands_repository.delete_user(user_uuid=user.uuid)
        user.delete_user(uuid=user.uuid)
        events: Sequence[BaseDomainEvent] = user.send_events()
        await self.event_store.save_event(event=events)
        await self.event_bus.send_event(event=events)
