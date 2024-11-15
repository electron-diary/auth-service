from typing import Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.base.uow_interface import UnitOfWorkInterface
from app.application.commands.delete_user_commands import DeleteUserCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.uuid_value_object import UUIDValueObject
from app.application.base.event_publisher_interface import EventPublisherInterface


class DeleteUserCommandHandler(BaseCommandHandler[DeleteUserCommand, None]):
    def __init__(
        self: Self, user_commands_repository: UserCommandsRepository, 
        uow: UnitOfWorkInterface, event_publisher: EventPublisherInterface
    ) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository
        self.unit_of_work: UnitOfWorkInterface = uow
        self.event_publisher: EventPublisherInterface = event_publisher

    async def __call__(self: Self, request: DeleteUserCommand) -> None:
        uuid: UUIDValueObject = UUIDValueObject(request.user_uuid)
        user: UserDomainEntity = UserDomainEntity()

        await self.user_commands_repository.delete_user(user_uuid=user.uuid)
        user.delete_user(user_uuid=user.uuid)
        await self.event_publisher.apply(event=user.send_events())
        await self.unit_of_work.commit()
