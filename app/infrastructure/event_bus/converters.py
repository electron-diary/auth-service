from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import UserCreated, UserDeleted, UsernameUpdated, UserRestored, ContactsUpdated
from app.infrastructure.event_bus.events import IntegrationEvent, UserCreatedIntegrationEvent, UserDeletedIntegrationEvent
from app.infrastructure.event_bus.events import UsernameUpdatedIntegrationEvent, UserRestoredIntegrationEvent,  ContactsUpdatedIntegrationEvent


def user_created_to_integration_event(user_created: UserCreated) -> UserCreatedIntegrationEvent:
    return UserCreatedIntegrationEvent(
        event_name=user_created.event_name,
        user_id=user_created.user_id,
        username=user_created.username,
        phone_number=user_created.phone_number,
        is_deleted=user_created.is_deleted,
    )

def user_deleted_to_integration_event(user_deleted: UserDeleted) -> UserDeletedIntegrationEvent:
    return UserDeletedIntegrationEvent(
        event_name=user_deleted.event_name,
        user_id=user_deleted.user_id,
        is_deleted=user_deleted.is_deleted,
    )

def user_restored_to_integration_event(user_restored: UserRestored) -> UserRestoredIntegrationEvent:
    return UserRestoredIntegrationEvent(
        event_name=user_restored.event_name,
        user_id=user_restored.user_id,
        is_deleted=user_restored.is_deleted,
    )

def username_updated_to_integration_event(username_updated: UsernameUpdated) -> UsernameUpdatedIntegrationEvent:
    return UsernameUpdatedIntegrationEvent(
        event_name=username_updated.event_name,
        user_id=username_updated.user_id,
        username=username_updated.username,
    )

def contacts_updated_to_integration_event(contacts_updated: ContactsUpdated) -> ContactsUpdatedIntegrationEvent:
    return ContactsUpdatedIntegrationEvent(
        event_name=contacts_updated.event_name,
        user_id=contacts_updated.user_id,
        phone_number=contacts_updated.phone_number,
    )

def domain_event_to_integration_event(event: DomainEvent) -> IntegrationEvent:
    match event:
        case UserCreated():
            return user_created_to_integration_event(event)
        case UserDeleted():
            return user_deleted_to_integration_event(event)
        case UserRestored():
            return user_restored_to_integration_event(event)
        case UsernameUpdated():
            return username_updated_to_integration_event(event)
        case ContactsUpdated():
            return contacts_updated_to_integration_event(event)
        case _:
            raise ValueError("Unknown event type")
        
