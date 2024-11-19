from typing import TYPE_CHECKING, Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.event_store_interface import EventStoreInterface
from app.application.commands.update_user_fullname_command import UpdateUserFullNameCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.constants.user_fullname import UserFullName
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_first_name_value_object import UserFirstNameValueObject
from app.domain.value_objects.user_last_name_value_object import UserLastNameValueObject
from app.domain.value_objects.user_middle_name_value_object import UserMiddleNameValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject

if TYPE_CHECKING:
    from collections.abc import Sequence

    from app.domain.base.base_event import BaseDomainEvent


class UpdateUserFullnameCommandHandler(BaseCommandHandler[UpdateUserFullNameCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository,
        event_bus: EventBusInterface,
        event_store: EventStoreInterface,
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.event_bus: EventBusInterface = event_bus
        self.event_store: EventStoreInterface = event_store

    async def __call__(self: Self, request: UpdateUserFullNameCommand) -> None:
        uuid: UUIDValueObject = UUIDValueObject(request.user_uuid)
        user_fullname: UserFullName = UserFullName(
            user_first_name=UserFirstNameValueObject(request.new_user_first_name),
            user_last_name=UserLastNameValueObject(request.new_user_last_name),
            user_middle_name=UserMiddleNameValueObject(request.new_user_middle_name),
        )
        events_to_replay: Sequence[BaseDomainEvent] = await self.event_store.get_events(uuid=uuid)
        user: UserDomainEntity = UserDomainEntity.replay_events(events=events_to_replay)

        await self.user_commands_repository.update_user_fullname(user=user)
        user.update_user_fullname(user_uuid=user.uuid, new_user_fullname=user_fullname)
        events: Sequence[BaseDomainEvent] = user.send_events()
        await self.event_store.save_event(event=events)
        await self.event_bus.send_event(event=events)
