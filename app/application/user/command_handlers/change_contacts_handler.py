from typing import Self

from app.application.event_bus import EventBus
from app.application.user.commands.change_contacts import ChangeContactsCommand
from app.application.user.exceptions import UserAlreadyExists
from app.domain.unit_of_work import UnitOfWorkInterface
from app.domain.user.repositories.user_repository import UserRepository


class ChangeContacts:
    def __init__(
        self: Self,
        unit_of_work: UnitOfWorkInterface,
        user_repository: UserRepository,
        event_bus: EventBus,
    ) -> None:
        self.unit_of_work = unit_of_work
        self.user_repository = user_repository
        self.event_bus = event_bus

    async def handle(self: Self, command: ChangeContactsCommand) -> None:
        user = await self.user_repository.load(command.user_id)
        if not user:
            raise UserAlreadyExists("User not found")

        if command.email and await self.user_repository.check_email_exists(command.email):
            raise UserAlreadyExists("User already exists")

        if command.phone and await self.user_repository.check_phone_number_exists(command.phone):
            raise UserAlreadyExists("User already exists")

        user.change_contacts(command.email, command.phone)

        await self.user_repository.update(user)
        await self.event_bus.publish(user.push_events())
        await self.unit_of_work.commit()
