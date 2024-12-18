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
class AddAddressCommand:
    profile_id: UUID
    profile_owner_id: UUID
    city: str
    country: str
    street: str
    house_number: str
    apartment_number: str
    postal_code: str


class AddAddress:
    def __init__(
        self,
        unit_of_work: UnitOfWorkCommitter,
        profile_repository: ProfileRepository,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.profile_repository = profile_repository
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: AddAddressCommand) -> None:
        user = await self.user_repository.load(command.profile_owner_id)
        if not user:
            raise UserNotFoundError("User not found")

        if user.status == Statuses.INACTIVE:
            raise UserInactiveError("User is inactive")

        profile = await self.profile_repository.load(command.profile_id)
        if not profile:
            raise ProfileNotFoundError("Profile not found")

        address_uuid = uuid4()

        profile.add_address(
            address_id=address_uuid,
            city=command.city,
            country=command.country,
            street=command.street,
            house_number=command.house_number,
            apartment_number=command.apartment_number,
            postal_code=command.postal_code,
        )

        await self.event_bus.publish(profile.push_events())
        await self.unit_of_work.commit()
