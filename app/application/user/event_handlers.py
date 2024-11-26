from typing import Self


from app.application.base.event_handlers import DomainEventHandler
from app.application.user.repositories import UserWriterRepository
from app.domain.user.actions import UserCreated, UserDeleted, UsernameUpdated, UserRestored, ContactsUpdated
from app.domain.user.value_objects import UserId, Username, Contacts, DeleteDate, CreatedDate
from app.domain.user.user import User


class UserCreatedEventHandler(DomainEventHandler[UserCreated]):
    def __init__(self: Self, user_writer_repository: UserWriterRepository) -> None:
        self.user_writer_repository: UserWriterRepository = user_writer_repository

    async def __call__(self: Self, event: UserCreated) -> None:
        user: User = User(
            id=UserId(event.user_id), 
            username=Username(event.username), 
            contacts=Contacts(email=event.email, phone=event.phone_number),
            delete_date=DeleteDate(event.deleted_date),
            created_at=CreatedDate(event.created_at),
        )
        await self.user_writer_repository.save_user(user=user)


class UserDeletedEventHandler(DomainEventHandler[UserDeleted]):
    def __init__(self: Self, user_writer_repository: UserWriterRepository) -> None:
        self.user_writer_repository: UserWriterRepository = user_writer_repository

    async def __call__(self: Self, event: UserDeleted) -> None:
        await self.user_writer_repository.delete_user(
            id=UserId(event.user_id), delete_date=DeleteDate(event.deleted_date)
        )


class UsernameUpdatedEventHandler(DomainEventHandler[UsernameUpdated]):
    def __init__(self: Self, user_writer_repository: UserWriterRepository) -> None:
        self.user_writer_repository: UserWriterRepository = user_writer_repository

    async def __call__(self: Self, event: UsernameUpdated) -> None:
        await self.user_writer_repository.update_username(
            id=UserId(event.user_id), username=Username(event.username)
        )


class UserRestoredEventHandler(DomainEventHandler[UserRestored]):
    def __init__(self: Self, user_writer_repository: UserWriterRepository) -> None:
        self.user_writer_repository: UserWriterRepository = user_writer_repository

    async def __call__(self: Self, event: UserRestored) -> None:
        await self.user_writer_repository.restore_user(
            id=UserId(event.user_id), delete_date=DeleteDate(event.deleted_date)
        )


class ContactsUpdatedEventHandler(DomainEventHandler[ContactsUpdated]):
    def __init__(self: Self, user_writer_repository: UserWriterRepository) -> None:
        self.user_writer_repository: UserWriterRepository = user_writer_repository

    async def __call__(self: Self, event: ContactsUpdated) -> None:
        await self.user_writer_repository.update_contacts(
            id=UserId(event.user_id), contacts=Contacts(email=event.email, phone=event.phone_number)
        )

