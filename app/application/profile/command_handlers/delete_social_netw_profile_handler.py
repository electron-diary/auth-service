from typing import Self

from app.application.event_bus import EventBus
from app.application.profile.commands.delete_social_netw_profile import DeleteSocialNetwProfileCommand
from app.application.profile.exceptions import ProfileNotFound
from app.application.user.exceptions import UserNotFound
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.user.enums.statuses import Statuses
from app.domain.user.exceptions import UserInactiveError
from app.domain.user.repositories.user_repository import UserRepository


class DeleteSocialNetwProfile:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkInterface,
        profile_repository: ProfileRepository,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.profile_repository = profile_repository
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: DeleteSocialNetwProfileCommand) -> None:
        user = await self.user_repository.load(command.profile_owner_id)
        if not user:
            raise UserNotFound("User not found")

        if user.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        profile = await self.profile_repository.load(command.profile_id)
        if not profile:
            raise ProfileNotFound("Profile not found")

        profile.delete_social_netw_profile(command.social_netw_profile_id)

        await self.event_bus.publish(profile.push_events())
        await self.unit_of_work.commit()

