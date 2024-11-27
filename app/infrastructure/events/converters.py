from typing import TypedDict
from dataclasses import asdict
from datetime import datetime

from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored
from app.infrastructure.events.integration_event import IntegrationEvent


def user_created_to_integration(event: UserCreated) -> IntegrationEvent:
    return IntegrationEvent(
        id=event.user_id,
        event_name="UserCreated",
        event=asdict(event),
    )

def user_deleted_to_integration(event: UserDeleted) -> IntegrationEvent:
    return IntegrationEvent(
        id=event.user_id,
        event_name="UserDeleted",
        event=asdict(event),
    )

def username_updated_to_integration(event: UsernameUpdated) -> IntegrationEvent:
    return IntegrationEvent(
        id=event.user_id,
        event_name="UsernameUpdated",
        event=asdict(event),
    )

def user_restored_to_integration(event: UserRestored) -> IntegrationEvent:
    return IntegrationEvent(
        id=event.user_id,
        event_name="UserRestored",
        event=asdict(event),
    )

def contacts_updated_to_integration(event: ContactsUpdated) -> IntegrationEvent:
    return IntegrationEvent(
        id=event.user_id,
        event_name="ContactsUpdated",
        event=asdict(event),
    )

def domain_event_to_integration(event: DomainEvent) -> IntegrationEvent:
    match event:
        case UserCreated():
            return user_created_to_integration(event=event)
        case UserDeleted():
            return user_deleted_to_integration(event=event)
        case UsernameUpdated():
            return username_updated_to_integration(event=event)
        case UserRestored():
            return user_restored_to_integration(event=event)
        case ContactsUpdated():
            return contacts_updated_to_integration(event=event)

def integration_event_to_domain(event: IntegrationEvent) -> DomainEvent:
    match event.event_name:
        case "UserCreated":
            return UserCreated(**event.event)
        case "UserDeleted":
            return UserDeleted(**event.event)
        case "UsernameUpdated":
            return UsernameUpdated(**event.event)
        case "UserRestored":
            return UserRestored(**event.event)
        case "ContactsUpdated":
            return ContactsUpdated(**event.event)
