from typing import Self
from dishka import Provider, Scope, provide

from app.application.user.repositories import UserReaderRepository, UserWriterRepository
from app.application.user.event_handlers import (
    ContactsUpdatedEventHandler,
    UserCreatedEventHandler,
    UserDeletedEventHandler,
    UsernameUpdatedEventHandler,
    UserRestoredEventHandler,
)


class EventHandlersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_user_created_event_handler(
        self: Self, user_writer: UserWriterRepository,
    ) -> UserCreatedEventHandler:
        return UserCreatedEventHandler(user_writer_repository=user_writer)

    @provide(scope=Scope.REQUEST)
    def provide_username_updated_event_handler(
        self: Self, user_writer: UserWriterRepository,
    ) -> UsernameUpdatedEventHandler:
        return UsernameUpdatedEventHandler(user_writer_repository=user_writer)

    @provide(scope=Scope.REQUEST)
    def provide_user_deleted_event_handler(
        self: Self, user_writer: UserWriterRepository,
    ) -> UserDeletedEventHandler:
        return UserDeletedEventHandler(user_writer_repository=user_writer)

    @provide(scope=Scope.REQUEST)
    def provide_user_restored_event_handler(
        self: Self, user_writer: UserWriterRepository,
    ) -> UserRestoredEventHandler:
        return UserRestoredEventHandler(user_writer_repository=user_writer)

    @provide(scope=Scope.REQUEST)
    def provide_contacts_updated_event_handler(
        self: Self, user_writer: UserWriterRepository,
    ) -> ContactsUpdatedEventHandler:
        return ContactsUpdatedEventHandler(user_writer_repository=user_writer)

