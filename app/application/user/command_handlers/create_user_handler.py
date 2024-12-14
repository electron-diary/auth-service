from typing import Self
from uuid import UUID, uuid4

from app.application.event_bus import EventBus
from app.application.unit_of_work import UnitOfWorkCommitterInterace
from app.application.user.commands.create_user import CreateUserCommand
from app.application.user.exceptions import UserAlreadyExists
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository


class CreateUser:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkCommitterInterace,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: CreateUserCommand) -> UUID:
        if command.email and await self.user_repository.check_email_exists(command.email):
            raise UserAlreadyExists("User already exists")

        if command.phone and await self.user_repository.check_phone_number_exists(command.phone):
            raise UserAlreadyExists("User already exists")

        if await self.user_repository.check_username_exists(command.username):
            raise UserAlreadyExists("User already exists")

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


