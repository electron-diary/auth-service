from typing import Self

from app.domain.user.entities.user import User
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.user.repositories.user_repository import UserRepository
from app.application.user.commands.change_username import ChangeUsernameCommand
from app.application.user.exceptions import UserAlreadyExists, UserNotFound
from app.application.event_bus import EventBus


class ChangeUsername:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkInterface,
        user_repository: UserRepository,
        event_bus: EventBus
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: ChangeUsernameCommand) -> None:
        user = await self.user_repository.load(command.user_id)
        if not user:
            raise UserNotFound('User not found')
        
        if await self.user_repository.check_username_exists(command.username):
            raise UserAlreadyExists('User already exists')
        
        user.change_username(command.username)

        await self.user_repository.update(user)
        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()