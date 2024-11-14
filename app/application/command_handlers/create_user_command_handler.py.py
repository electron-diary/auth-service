from typing import Self
from uuid import UUID

from app.application.base.base_command_handler import BaseCommandHandler
from app.application.commands.create_user_command import CreateUserCommand
from app.application.interfaces.user_commands_repository import UserCommandsRepository


class CreateUserCommandHandler(BaseCommandHandler[CreateUserCommand, UUID]):
    def __init__(self: Self, user_commands_repository: UserCommandsRepository) -> None:
        self.user_commands_repository: UserCommandsRepository = user_commands_repository

    async def __call__(self: Self, request: CreateUserCommand) -> UUID:
        ...