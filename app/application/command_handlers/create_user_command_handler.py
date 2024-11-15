from collections.abc import Sequence
from typing import Self
from uuid import UUID

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.event_bus_interface import EventBusInterface
from app.application.base.event_store_interface import EventStoreInterface
from app.application.base.uow_interface import UnitOfWorkInterface
from app.application.commands.create_user_command import CreateUserCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.base.base_event import BaseDomainEvent
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_first_name_value_object import UserFirstNameValueObject
from app.domain.value_objects.user_last_name_value_object import UserLastNameValueObject
from app.domain.value_objects.user_middle_name_value_object import UserMiddleNameValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject


class CreateUserCommandHandler(BaseCommandHandler[CreateUserCommand, UUID]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository,
        uow: UnitOfWorkInterface, event_bus: EventBusInterface,
        event_store: EventStoreInterface,
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.unit_of_work: UnitOfWorkInterface = uow
        self.event_bus: EventBusInterface = event_bus
        self.event_store: EventStoreInterface = event_store

    async def __call__(self: Self, request: CreateUserCommand) -> UUID:
        user_fullname: UserFullName = UserFullName(
            user_first_name=UserFirstNameValueObject(request.user_first_name),
            user_last_name=UserLastNameValueObject(request.user_last_name),
            user_middle_name=UserMiddleNameValueObject(request.user_middle_name),
        )
        user_contact: UserContact = UserContact(
            user_email=UserEmailValueObject(request.user_email),
            user_phone=UserPhoneValueObject(request.user_phone),
        )
        new_user: UserDomainEntity = UserDomainEntity.create_user(
            user_uuid=UUIDValueObject(request.user_uuid),
            user_contact=user_contact,
            user_fullname=user_fullname,
        )
        events: Sequence[BaseDomainEvent] = new_user.send_events()

        await self.user_commands_repository.create_user(user=new_user)
        await self.event_store.save_event(event=events)
        await self.event_bus.send_event(event=events)
        await self.unit_of_work.commit()
        return request.user_uuid

