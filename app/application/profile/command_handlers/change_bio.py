from typing import Self

from app.application.event_bus import EventBus
from app.application.profile.commands.change_bio import ChangeBioCommand
from app.application.profile.exceptions import ProfileNotFoundError
from app.application.unit_of_work import UnitOfWorkCommitter
from app.application.user.exceptions import UserNotFoundError
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.domain.user.enums.statuses import Statuses
from app.domain.user.exceptions import UserInactiveError
from app.domain.user.repositories.user_repository import UserRepository


class ChangeBio:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkCommitter,
        profile_repository: ProfileRepository,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.profile_repository = profile_repository
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: ChangeBioCommand) -> None:
        user = await self.user_repository.load(command.profile_owner_id)
        if not user:
            raise UserNotFoundError("User not found")

        if user.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        profile = await self.profile_repository.load(command.profile_id)
        if not profile:
            raise ProfileNotFoundError("Profile not found")

        profile.change_bio(command.bio)

        await self.event_bus.publish(profile.push_events())
        await self.unit_of_work.commit()
