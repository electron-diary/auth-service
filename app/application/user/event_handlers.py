from typing import Self

from app.application.base.event_handler import EventHandler
from app.application.user.interfaces import UserProjectionsGatewayInterface
from app.domain.user.actions import ContactsUpdated, UserCreated, UserDeleted, UsernameUpdated, UserRestored


class UserCreatedEventHandler(EventHandler[UserCreated]):
    def __init__(self: Self, user_projections_gateway: UserProjectionsGatewayInterface) -> None:
        self.user_projections_gateway: UserProjectionsGatewayInterface = user_projections_gateway

    async def __call__(self: Self, event: UserCreated) -> None:
        await self.user_projections_gateway.add_user(event=event)


class UserDeletedEventHandler(EventHandler[UserDeleted]):
    def __init__(self: Self, user_projections_gateway: UserProjectionsGatewayInterface) -> None:
        self.user_projections_gateway: UserProjectionsGatewayInterface = user_projections_gateway

    async def __call__(self: Self, event: UserDeleted) -> None:
        await self.user_projections_gateway.delete_user(event=event)


class UsernameUpdatedEventHandler(EventHandler[UsernameUpdated]):
    def __init__(self: Self, user_projections_gateway: UserProjectionsGatewayInterface) -> None:
        self.user_projections_gateway: UserProjectionsGatewayInterface = user_projections_gateway

    async def __call__(self: Self, event: UsernameUpdated) -> None:
        await self.user_projections_gateway.update_username(event=event)


class ContactsUpdatedEventHandler(EventHandler[ContactsUpdated]):
    def __init__(self: Self, user_projections_gateway: UserProjectionsGatewayInterface) -> None:
        self.user_projections_gateway: UserProjectionsGatewayInterface = user_projections_gateway

    async def __call__(self: Self, event: ContactsUpdated) -> None:
        await self.user_projections_gateway.update_contacts(event=event)


class UserRestoredEventHandler(EventHandler[UserRestored]):
    def __init__(self: Self, user_projections_gateway: UserProjectionsGatewayInterface) -> None:
        self.user_projections_gateway: UserProjectionsGatewayInterface = user_projections_gateway

    async def __call__(self: Self, event: UserRestored) -> None:
        await self.user_projections_gateway.restore_user(event=event)

