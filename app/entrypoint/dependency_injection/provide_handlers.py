from typing import Self

from dishka import Provider, Scope, provide

from app.application.base .event_bus import GlobalEventBusInterface, LocalEventBusInterface
from app.application.user.command_handlers import (
    CreateUserCommandHandler,
    DeleteUserCommandHandler,
    RestoreUserCommandHandler,
    UpdateContactsCommandHandler,
    UpdateUsernameCommandHandler,
)
from app.application.user.event_handlers import (
    ContactsUpdatedEventHandler,
    UserCreatedEventHandler,
    UserDeletedEventHandler,
    UsernameUpdatedEventHandler,
    UserRestoredEventHandler,
)
from app.application.user.interfaces import (
    UserProjectionsGatewayInterface,
    UserReaderGatewayInterface,
    UserWriterGatewayInterface,
)
from app.application.user.query_handlers import GetUserByIdQueryHandler


class CommandHandlersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_create_user_command_handler(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        global_event_bus: GlobalEventBusInterface,
        local_event_bus: LocalEventBusInterface,
    ) -> CreateUserCommandHandler:
        return CreateUserCommandHandler(
            user_writer_gateway=user_writer_gateway,
            local_event_bus=local_event_bus, global_event_bus=global_event_bus,
        )

    @provide(scope=Scope.REQUEST)
    def provide_update_username_command_handler(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        global_event_bus: GlobalEventBusInterface,
        local_event_bus: LocalEventBusInterface,
    ) -> UpdateUsernameCommandHandler:
        return UpdateUsernameCommandHandler(
            user_writer_gateway=user_writer_gateway,
            local_event_bus=local_event_bus, global_event_bus=global_event_bus,
        )

    @provide(scope=Scope.REQUEST)
    def provide_update_contacts_command_handler(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        global_event_bus: GlobalEventBusInterface,
        local_event_bus: LocalEventBusInterface,
    ) -> UpdateContactsCommandHandler:
        return UpdateContactsCommandHandler(
            user_writer_gateway=user_writer_gateway,
            local_event_bus=local_event_bus, global_event_bus=global_event_bus,
        )

    @provide(scope=Scope.REQUEST)
    def provide_delete_user_command_handler(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        global_event_bus: GlobalEventBusInterface,
        local_event_bus: LocalEventBusInterface,
    ) -> DeleteUserCommandHandler:
        return DeleteUserCommandHandler(
            user_writer_gateway=user_writer_gateway,
            local_event_bus=local_event_bus, global_event_bus=global_event_bus,
        )

    @provide(scope=Scope.REQUEST)
    def provide_restore_user_command_handler(
        self: Self,
        user_writer_gateway: UserWriterGatewayInterface,
        global_event_bus: GlobalEventBusInterface,
        local_event_bus: LocalEventBusInterface,
    ) -> RestoreUserCommandHandler:
        return RestoreUserCommandHandler(
            user_writer_gateway=user_writer_gateway,
            local_event_bus=local_event_bus, global_event_bus=global_event_bus,
        )

class EventHandlersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_user_created_event_handler(
        self: Self,
        user_projections_gateway: UserProjectionsGatewayInterface,
    ) -> UserCreatedEventHandler:
        return UserCreatedEventHandler(user_projections_gateway=user_projections_gateway)

    @provide(scope=Scope.REQUEST)
    def provide_user_deleted_event_handler(
        self: Self, user_projections_gateway: UserProjectionsGatewayInterface,
    ) -> UserDeletedEventHandler:
        return UserDeletedEventHandler(user_projections_gateway=user_projections_gateway)

    @provide(scope=Scope.REQUEST)
    def provide_user_restored_event_handler(
        self: Self, user_projections_gateway: UserProjectionsGatewayInterface,
    ) -> UserRestoredEventHandler:
        return UserRestoredEventHandler(user_projections_gateway=user_projections_gateway)

    @provide(scope=Scope.REQUEST)
    def provide_username_updated_event_handler(
        self: Self, user_projections_gateway: UserProjectionsGatewayInterface,
    ) -> UsernameUpdatedEventHandler:
        return UsernameUpdatedEventHandler(user_projections_gateway=user_projections_gateway)

    @provide(scope=Scope.REQUEST)
    def provide_contacts_updated_event_handler(
        self: Self, user_projections_gateway: UserProjectionsGatewayInterface,
    ) -> ContactsUpdatedEventHandler:
        return ContactsUpdatedEventHandler(user_projections_gateway=user_projections_gateway)


class QueryHandlersProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def provide_get_user_by_id_query_handler(
        self: Self, user_reader_gateway: UserReaderGatewayInterface,
    ) -> GetUserByIdQueryHandler:
        return GetUserByIdQueryHandler(user_reader_gateway=user_reader_gateway)
