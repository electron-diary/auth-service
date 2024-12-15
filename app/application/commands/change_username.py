from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.application.common.event_bus import EventBus
from app.application.common.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.application.common.unit_of_work import UnitOfWorkCommitter
from app.domain.user.repositories.user_repository import UserRepository


@dataclass(frozen=True)
class ChangeUsernameCommand:
    user_id: UUID
    username: str


class ChangeUsername:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkCommitter,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: ChangeUsernameCommand) -> None:
        user = await self.user_repository.load(command.user_id)
        if not user:
            raise UserNotFoundError("User not found")

        if await self.user_repository.check_username_exists(command.username):
            raise UserAlreadyExistsError("User already exists")

        user.change_username(command.username)

        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()
