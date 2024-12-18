from dataclasses import dataclass
from typing import Self
from uuid import UUID

from app.application.common.event_bus import EventBus
from app.application.common.exceptions import UserAlreadyExistsError, UserNotFoundError
from app.application.common.unit_of_work import UnitOfWorkCommitter
from app.domain.user.repositories.user_repository import UserRepository


@dataclass(frozen=True)
class ChangeContactsCommand:
    user_id: UUID
    email: str | None
    phone: int | None


class ChangeContacts:
    def __init__(
        self,
        unit_of_work: UnitOfWorkCommitter,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: ChangeContactsCommand) -> None:
        user = await self.user_repository.load(command.user_id)
        if not user:
            raise UserNotFoundError("User not found")

        if command.email and await self.user_repository.check_email_exists(command.email):
            raise UserAlreadyExistsError("User already exists")

        if command.phone and await self.user_repository.check_phone_number_exists(command.phone):
            raise UserAlreadyExistsError("User already exists")

        user.change_contacts(command.email, command.phone)

        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()
