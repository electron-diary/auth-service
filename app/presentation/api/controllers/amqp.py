from dishka.integrations.faststream import FromDishka, inject
from faststream.rabbit import RabbitRouter

from app.domain.user.actions import UserCreated, UserDeleted, UsernameUpdated, UserRestored, ContactsUpdated
from app.infrastructure.events.converters import integration_event_to_domain
from app.infrastructure.events.integration_event import IntegrationEvent
from app.application.user.event_handlers import (
    ContactsUpdatedEventHandler,
    UserCreatedEventHandler,
    UserDeletedEventHandler,
    UsernameUpdatedEventHandler,
    UserRestoredEventHandler,
)

router: RabbitRouter = RabbitRouter()


@router.subscriber(queue='user-created')
@inject
async def handle_user_created_event(event: IntegrationEvent, handler: FromDishka[UserCreatedEventHandler]) -> None:
    domain_event: UserCreated = integration_event_to_domain(event=event)
    await handler(event=domain_event)

@router.subscriber(queue='user-deleted')
@inject
async def handle_user_deleted_event(event: IntegrationEvent, handler: FromDishka[UserDeletedEventHandler]) -> None:
    domain_event: UserDeleted = integration_event_to_domain(event=event)
    await handler(event=domain_event)

@router.subscriber(queue='username-updated')
@inject
async def handle_username_updated_event(event: IntegrationEvent, handler: FromDishka[UsernameUpdatedEventHandler]) -> None:
    domain_event: UsernameUpdated = integration_event_to_domain(event=event)
    await handler(event=domain_event)

@router.subscriber(queue='user-restored')
@inject
async def handle_user_restored_event(event: IntegrationEvent, handler: FromDishka[UserRestoredEventHandler]) -> None:
    domain_event: UserRestored = integration_event_to_domain(event=event)
    await handler(event=domain_event)

@router.subscriber(queue='contacts-updated')
@inject
async def handle_contacts_updated_event(event: IntegrationEvent, handler: FromDishka[ContactsUpdatedEventHandler]) -> None:
    domain_event: ContactsUpdated = integration_event_to_domain(event=event)
    await handler(event=domain_event)

