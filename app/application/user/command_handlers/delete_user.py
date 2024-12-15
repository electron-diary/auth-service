from typing import Self

from app.application.event_bus import EventBus
from app.application.unit_of_work import UnitOfWorkCommitter
from app.application.user.commands.delete_user import DeleteUserCommand
from app.application.user.exceptions import UserNotFoundError
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.domain.user.repositories.user_repository import UserRepository


class DeleteUser:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkCommitter,
        user_repository: UserRepository,
        event_bus: EventBus,
        profile_repository: ProfileRepository,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus
        self.profile_repository = profile_repository

    async def handle(self: Self, command: DeleteUserCommand) -> None:
        user = await self.user_repository.load(command.id)
        if not user:
            raise UserNotFoundError("User not found")

        profiles = await self.profile_repository.load_all_user_profiles(user.id)

        user.delete_user()

        if profiles:
            for profile in profiles:
                profile.delete_profile()

        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()
