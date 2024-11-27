from typing import Self

from dishka import Provider, Scope, provide

from app.application.user.event_handlers import (
    ContactsUpdatedEventHandler,
    UserCreatedEventHandler,
    UserDeletedEventHandler,
    UsernameUpdatedEventHandler,
    UserRestoredEventHandler,
)
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored
from app.infrastructure.events.event_observable import ObservableImpl
from app.infrastructure.events.observable_interface import ObservableInterface

'''
ТОЖЕ ХУИТА
'''
class ObservableProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def setup_observable(
        self: Self,
        user_created_event_handler: UserCreatedEventHandler,
        user_deleted_event_handler: UserDeletedEventHandler,
        username_updated_event_handler: UsernameUpdatedEventHandler,
        user_restored_event_handler: UserRestoredEventHandler,
        contacts_updated_event_handler: ContactsUpdatedEventHandler,
    ) -> ObservableInterface:
        observable: ObservableImpl = ObservableImpl()
        observable.add_event_handler(UserCreated, user_created_event_handler)
        observable.add_event_handler(UserDeleted, user_deleted_event_handler)
        observable.add_event_handler(UsernameUpdated, username_updated_event_handler)
        observable.add_event_handler(UserRestored, user_restored_event_handler)
        observable.add_event_handler(ContactsUpdated, contacts_updated_event_handler)
        return observable
