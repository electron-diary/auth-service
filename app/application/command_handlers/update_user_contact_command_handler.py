from typing import TYPE_CHECKING, Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.event_store_interface import EventStoreInterface
from app.application.commands.update_user_conact_command import UpdateUserContactCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.constants.user_contact import UserContact
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject

if TYPE_CHECKING:
    from collections.abc import Sequence

    from app.domain.base.base_event import BaseDomainEvent


class UpdateUserContactCommandHandler(BaseCommandHandler[UpdateUserContactCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository,
        event_bus: EventBusInterface,
        event_store: EventStoreInterface,
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.event_bus: EventBusInterface = event_bus
        self.event_store: EventStoreInterface = event_store

    async def __call__(self: Self, request: UpdateUserContactCommand) -> None:
        uuid: UUIDValueObject = UUIDValueObject(request.user_uuid)
        user_contact: UserContact = UserContact(
            user_email=UserEmailValueObject(request.new_user_email),
            user_phone=UserPhoneValueObject(request.new_user_phone),
        )
        events_to_replay: Sequence[BaseDomainEvent] = await self.event_store.get_events(uuid=uuid)
        user: UserDomainEntity = UserDomainEntity.replay_events(events=events_to_replay)

        await self.user_commands_repository.update_user_contact(user=UserDomainEntity)
        user.update_user_contact(user_uuid=user.uuid, new_user_contact=user_contact)
        events: Sequence[BaseDomainEvent] = user.send_events()
        await self.event_store.save_event(event=events)
        await self.event_bus.send_event(event=events)
