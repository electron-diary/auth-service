from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4

from app.application.common.event_bus import EventBus
from app.application.common.exceptions import UserNotFoundError
from app.application.common.unit_of_work import UnitOfWorkCommitter
from app.domain.profile.entities.profile import Profile
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.domain.user.statuses import Statuses
from app.domain.user.exceptions import UserInactiveError
from app.domain.user.repositories.user_repository import UserRepository


@dataclass(frozen=True)
class CreateProfileCommand:
    profile_owner_id: UUID
    first_name: str
    last_name: str
    middle_name: str | None
    bio: str


class CreateProfile:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkCommitter,
        user_repository: UserRepository,
        profile_repository: ProfileRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.profile_repository = profile_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: CreateProfileCommand) -> UUID:
        user = await self.user_repository.load(command.profile_owner_id)
        if not user:
            raise UserNotFoundError("User not found")

        if user.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        profile_uuid = uuid4()

        profile: Profile = Profile.create_profile(
            uow=self.unit_of_work,
            profile_owner_id=user.id,
            profile_id=profile_uuid,
            first_name=command.first_name,
            last_name=command.last_name,
            middle_name=command.middle_name,
            bio=command.bio,
        )

        await self.event_bus.publish(profile.push_events())
        await self.unit_of_work.commit()

        return profile_uuid
