from typing import Self

from dishka import Provider, Scope, provide

from app.application.base.event_queue import GlobalEventBusRepository
from app.application.base.event_store import EventStoreRepository
from app.application.user.command_handlers import (
    CreateUserCommandHandler,
    DeleteUserCommandHandler,
    RestoreUserCommandHandler,
    UpdateContactsCommandHandler,
    UpdateUsernameCommandHandler,
)
from app.application.user.query_handlers import (
    GetUserActionsQueryHandler,
    GetUserByIdQueryHandler,
    GetUsersQueryHandler,
)
from app.application.user.repositories import UserReaderRepository


class CommandHandlersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_create_user_command_handler(
        self: Self, event_store: EventStoreRepository, event_bus: GlobalEventBusRepository,
    ) -> CreateUserCommandHandler:
        return CreateUserCommandHandler(event_store=event_store, event_bus=event_bus)

    @provide(scope=Scope.REQUEST)
    def provide_update_contacts_command_handler(
        self: Self, event_store: EventStoreRepository, event_bus: GlobalEventBusRepository,
    ) -> UpdateContactsCommandHandler:
        return UpdateContactsCommandHandler(event_store=event_store, event_bus=event_bus)

    @provide(scope=Scope.REQUEST)
    def provide_delete_user_command_handler(
        self: Self, event_store: EventStoreRepository, event_bus: GlobalEventBusRepository,
    ) -> DeleteUserCommandHandler:
        return DeleteUserCommandHandler(event_store=event_store, event_bus=event_bus)

    @provide(scope=Scope.REQUEST)
    def provide_restore_user_command_handler(
        self: Self, event_store: EventStoreRepository, event_bus: GlobalEventBusRepository,
    ) -> RestoreUserCommandHandler:
        return RestoreUserCommandHandler(event_store=event_store, event_bus=event_bus)

    @provide(scope=Scope.REQUEST)
    def provide_update_username_command_handler(
        self: Self, event_store: EventStoreRepository, event_bus: GlobalEventBusRepository,
    ) -> UpdateUsernameCommandHandler:
        return UpdateUsernameCommandHandler(event_store=event_store, event_bus=event_bus)

class QueryHandlersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_get_user_by_id_query_handler(
        self: Self, user_reader: UserReaderRepository,
    ) -> GetUserByIdQueryHandler:
        return GetUserByIdQueryHandler(user_reader_repository=user_reader)

    @provide(scope=Scope.REQUEST)
    def provide_get_user_actions_query_handler(
        self: Self, event_store: EventStoreRepository,
    ) -> GetUserActionsQueryHandler:
        return GetUserActionsQueryHandler(event_store=event_store)

    @provide(scope=Scope.REQUEST)
    def provide_get_users_query_handler(
        self: Self, user_reader: UserReaderRepository,
    ) -> GetUsersQueryHandler:
        return GetUsersQueryHandler(user_reader_repository=user_reader)


