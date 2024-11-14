from typing import Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.application.commands.update_user_fullname_command import UpdateUserFullNameCommand


class UpdateUserFullnameCommandHandler(BaseCommandHandler[UpdateUserFullNameCommand, None]):
    def __init__(self: Self, user_commands_repository: UserCommandsRepository) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository

    async def __call__(self: Self, request: UpdateUserFullNameCommand) -> None:
        ...