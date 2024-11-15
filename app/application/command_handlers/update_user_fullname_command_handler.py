from typing import Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.commands.update_user_fullname_command import UpdateUserFullNameCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.domain.constants.user_fullname import UserFullName
from app.domain.entities.user_entity import UserDomainEntity
from app.domain.value_objects.user_first_name_value_object import UserFirstNameValueObject
from app.domain.value_objects.user_last_name_value_object import UserLastNameValueObject
from app.domain.value_objects.user_middle_name_value_object import UserMiddleNameValueObject


class UpdateUserFullnameCommandHandler(BaseCommandHandler[UpdateUserFullNameCommand, None]):
    def __init__(self: Self, user_commands_repository: UserCommandsRepository) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository

    async def __call__(self: Self, request: UpdateUserFullNameCommand) -> None:
        user_fullname: UserFullName = UserFullName(
            user_first_name=UserFirstNameValueObject(request.new_user_first_name),
            user_last_name=UserLastNameValueObject(request.new_user_last_name),
            user_middle_name=UserMiddleNameValueObject(request.new_user_middle_name),
        )
        user: UserDomainEntity = UserDomainEntity()

        await self.user_commands_repository.update_user_fullname(user=user)
        user.update_user_fullname(user_uuid=user.user_uuid, new_user_fullname=user_fullname)
