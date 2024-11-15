from typing import Self, Sequence

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.uow_interface import UnitOfWorkInterface
from app.application.commands.delete_user_commands import DeleteUserCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.uuid_value_object import UUIDValueObject
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.event_store_interface import EventStoreInterface
from app.domain.common.common_event import CommonDomainEvent


class DeleteUserCommandHandler(BaseCommandHandler[DeleteUserCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository, 
        uow: UnitOfWorkInterface, event_bus: EventBusInterface,
        event_store: EventStoreInterface
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.unit_of_work: UnitOfWorkInterface = uow
        self.event_bus: EventBusInterface = event_bus
        self.event_store: EventStoreInterface = event_store

    async def __call__(self: Self, request: DeleteUserCommand) -> None:
        uuid: UUIDValueObject = UUIDValueObject(request.user_uuid)
        user: UserDomainEntity = UserDomainEntity()
        events: Sequence[CommonDomainEvent] = user.send_events()

        await self.user_commands_repository.delete_user(user_uuid=user.uuid)
        user.delete_user(user_uuid=user.uuid)
        await self.event_store.save_event(event=events)
        await self.event_bus.send_event(event=events)
        await self.unit_of_work.commit()
