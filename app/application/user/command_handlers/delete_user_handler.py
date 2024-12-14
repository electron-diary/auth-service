from typing import Self

from app.application.event_bus import EventBus
from app.application.user.commands.delete_user import DeleteUserCommand
from app.application.user.exceptions import UserNotFound
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.user.repositories.user_repository import UserRepository


class DeleteUser:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkInterface,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: DeleteUserCommand) -> None:
        user = await self.user_repository.load(command.id)
        if not user:
            raise UserNotFound("User not found")

        user.delete_user()

        await self.user_repository.delete(command.user_id)
        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()
