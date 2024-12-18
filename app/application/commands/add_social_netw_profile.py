from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4

from app.application.common.event_bus import EventBus
from app.application.common.exceptions import ProfileNotFoundError, UserNotFoundError
from app.application.common.unit_of_work import UnitOfWorkCommitter
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.domain.user.exceptions import UserInactiveError
from app.domain.user.repositories.user_repository import UserRepository
from app.domain.user.statuses import Statuses


@dataclass(frozen=True)
class AddSocialNetwProfileCommand:
    profile_id: UUID
    profile_owner_id: UUID
    social_netw_name: str
    social_netw_url: str


class AddSocialNetwProfile:
    def __init__(
        self,
        user_repository: UserRepository,
        profile_repository: ProfileRepository,
        unit_of_work: UnitOfWorkCommitter,
        event_bus: EventBus,
    ):
        self.user_repository = user_repository
        self.profile_repository = profile_repository
        self.unit_of_work = unit_of_work
        self.event_bus = event_bus

    async def handle(self: Self, command: AddSocialNetwProfileCommand) -> None:
        user = await self.user_repository.load(command.profile_owner_id)
        if not user:
            raise UserNotFoundError("User not found")

        if user.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        profile = await self.profile_repository.load(command.profile_id)
        if not profile:
            raise ProfileNotFoundError("Profile not found")

        social_netw_profile_id = uuid4()

        profile.add_social_netw_profile(
            social_netw_profile_id=social_netw_profile_id,
            social_netw_profile_name=command.social_netw_profile_name,
            social_netw_profile_url=command.social_netw_profile_link,
        )

        await self.event_bus.publish(profile.push_events())
        await self.unit_of_work.commit()
