from typing import Self
from uuid import UUID
from collections.abc import Sequence

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.uow_interface import UnitOfWorkInterface
from app.application.commands.create_user_command import CreateUserCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.constants.user_contact import UserContact
from app.domain.constants.user_fullname import UserFullName
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_first_name_value_object import UserFirstNameValueObject
from app.domain.value_objects.user_last_name_value_object import UserLastNameValueObject
from app.domain.value_objects.user_middle_name_value_object import UserMiddleNameValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.uuid_value_object import UUIDValueObject
from app.application.base.event_publisher_interface import EventPublisherInterface


class CreateUserCommandHandler(BaseCommandHandler[CreateUserCommand, UUID]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository, 
        uow: UnitOfWorkInterface, event_publisher: EventPublisherInterface
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.unit_of_work: UnitOfWorkInterface = uow
        self.event_publisher: EventPublisherInterface = event_publisher

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

        await self.user_commands_repository.create_user(user=new_user)
        await self.event_publisher.apply(event=new_user.send_events())
        await self.unit_of_work.commit()
        return request.user_uuid

