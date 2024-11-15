from typing import Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.uow_interface import UnitOfWorkInterface
from app.application.commands.update_user_conact_command import UpdateUserContactCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.constants.user_contact import UserContact
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.application.base.event_publisher_interface import EventPublisherInterface


class UpdateUserContactCommandHandler(BaseCommandHandler[UpdateUserContactCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository,
         uow: UnitOfWorkInterface, event_publisher: EventPublisherInterface
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.unit_of_work: UnitOfWorkInterface = uow
        self.event_publisher: EventPublisherInterface = event_publisher

    async def __call__(self: Self, request: UpdateUserContactCommand) -> None:
        user_contact: UserContact = UserContact(
            user_email=UserEmailValueObject(request.new_user_email),
            user_phone=UserPhoneValueObject(request.new_user_phone),
        )
        user: UserDomainEntity = UserDomainEntity()

        await self.user_commands_repository.update_user_contact(user=UserDomainEntity)
        user.update_user_contact(user_uuid=user.user_uuid, new_user_contact=user_contact)
        await self.event_publisher.apply(event=user.send_events())
        await self.unit_of_work.commit()
