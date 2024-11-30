from dishka.integrations.faststream import FromDishka, inject
from faststream.rabbit import RabbitRouter

from app.application.user.event_handlers import (
    ContactsUpdatedEventHandler,
    UserCreatedEventHandler,
    UserDeletedEventHandler,
    UsernameUpdatedEventHandler,
    UserRestoredEventHandler,
)
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored

router: RabbitRouter = RabbitRouter()


@router.subscriber("user-created", retry=5)
@inject
async def user_created_worker(
    event: UserCreated, handler: FromDishka[UserCreatedEventHandler],
) -> None:
    await handler(event=event)

@router.subscriber("user-deleted", retry=5)
@inject
async def user_deleted_worker(
    event: UserDeleted, handler: FromDishka[UserDeletedEventHandler],
) -> None:
    await handler(event=event)

@router.subscriber("username-updated", retry=5)
@inject
async def username_updated_worker(
    event: UsernameUpdated, handler: FromDishka[UsernameUpdatedEventHandler],
) -> None:
    await handler(event=event)

@router.subscriber("user-restored", retry=5)
@inject
async def user_restored_worker(
    event: UserRestored, handler: FromDishka[UserRestoredEventHandler],
) -> None:
    await handler(event=event)

@router.subscriber("contacts-updated", retry=5)
@inject
async def contacts_updated_worker(
    event: ContactsUpdated, handler: FromDishka[ContactsUpdatedEventHandler],
) -> None:
    await handler(event=event)
