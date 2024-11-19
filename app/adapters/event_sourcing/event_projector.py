from typing import Self

from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.application.base.projector_interface import ProjectorInterface
from app.application.base.integration_event import IntegrationEvent
from app.application.interfaces.user_projections_repository import UserProjectionsRepository


class EventsProjector(ProjectorInterface):
    def __init__(self: Self, user_projections_repository: UserProjectionsRepository) -> None:
        self.user_projections_repository: UserProjectionsRepository = user_projections_repository

    async def project(self: Self, event: IntegrationEvent) -> None:
        match event.event_name:
            case "CreateUserEvent":
                create_user_event: CreateUserEvent = CreateUserEvent(**event.event_data)
                await self.user_projections_repository.create_user(create_user_event)
            case "UpdateUserFullNameEvent":
                update_user_fullname_event: UpdateUserFullNameEvent = UpdateUserFullNameEvent(**event.event_data)
                await self.user_projections_repository.update_user_fullname(update_user_fullname_event)
            case "UpdateUserContactEvent":
                update_user_contact_event: UpdateUserContactEvent = UpdateUserContactEvent(**event.event_data)
                await self.user_projections_repository.update_user_contact(update_user_contact_event)
            case "DeleteUserEvent":
                delete_user_event: DeleteUserEvent = DeleteUserEvent(**event.event_data)
                await self.user_projections_repository.delete_user(delete_user_event)