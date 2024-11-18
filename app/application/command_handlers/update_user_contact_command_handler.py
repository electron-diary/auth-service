from collections.abc import Sequence
from typing import Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.event_store_interface import EventStoreInterface
from app.application.base.uow_interface import UnitOfWorkInterface
from app.application.commands.update_user_conact_command import UpdateUserContactCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.base.base_event import BaseDomainEvent
from app.domain.constants.user_contact import UserContact
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


class UpdateUserContactCommandHandler(BaseCommandHandler[UpdateUserContactCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository,
        uow: UnitOfWorkInterface, event_bus: EventBusInterface,
        event_store: EventStoreInterface,
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.unit_of_work: UnitOfWorkInterface = uow
        self.event_bus: EventBusInterface = event_bus
        self.event_store: EventStoreInterface = event_store

    async def __call__(self: Self, request: UpdateUserContactCommand) -> None:
        uuid: UUIDValueObject = UUIDValueObject(request.user_uuid)
        user_contact: UserContact = UserContact(
            user_email=UserEmailValueObject(request.new_user_email),
            user_phone=UserPhoneValueObject(request.new_user_phone),
        )
        user: UserDomainEntity = await self.event_store.get_current_state(uuid=uuid)

        await self.user_commands_repository.update_user_contact(user=UserDomainEntity)
        user.update_user_contact(user_uuid=user.user_uuid, new_user_contact=user_contact)
        events: Sequence[BaseDomainEvent] = user.send_events()
        await self.event_store.save_event(event=events)
        await self.event_bus.send_event(event=events)
        await self.unit_of_work.commit()
