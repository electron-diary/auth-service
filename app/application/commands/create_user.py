from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4

from app.application.common.event_bus import EventBus
from app.application.common.exceptions import UserAlreadyExistsError
from app.application.common.unit_of_work import UnitOfWorkCommitter
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository


@dataclass(frozen=True)
class CreateUserCommand:
    username: str
    email: str | None
    phone: int | None


class CreateUser:
    def __init__(
        self,
        unit_of_work: UnitOfWorkCommitter,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: CreateUserCommand) -> UUID:
        if command.email and await self.user_repository.check_email_exists(command.email):
            raise UserAlreadyExistsError("User already exists")

        if command.phone and await self.user_repository.check_phone_number_exists(command.phone):
            raise UserAlreadyExistsError("User already exists")

        if await self.user_repository.check_username_exists(command.username):
            raise UserAlreadyExistsError("User already exists")

        user_uuid = uuid4()

        user: User = User.create_user(
            uow=self.unit_of_work,
            user_id=user_uuid,
            username=command.username,
            email=command.email,
            phone=command.phone,
        )

        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()


