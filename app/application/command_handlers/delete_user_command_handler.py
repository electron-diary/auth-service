from typing import Self

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.interfaces.user_commands_repository import UserCommandsRepository
from app.application.commands.delete_user_commands import DeleteUserCommand


class DeleteUserCommandHandler(BaseCommandHandler[DeleteUserCommand, None]):
    def __init__(self: Self, user_commands_repository: UserCommandsRepository) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository

    async def __call__(self: Self, request: DeleteUserCommand) -> None:
        ...