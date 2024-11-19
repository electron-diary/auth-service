from app.application.base.integration_event import IntegrationEvent
from app.domain.events.update_user_fullname import UpdateUserFullNameEvent
from app.domain.events.create_user_event import CreateUserEvent
from app.domain.events.delete_user_event import DeleteUserEvent
from app.domain.events.update_user_contact import UpdateUserContactEvent


def convert_integartion_event_to_domain_event(event: IntegrationEvent) -> None:
    match event.event_name:
        case "CreateUserEvent":
            create_user_event: CreateUserEvent = CreateUserEvent(**event.event_data)
            return create_user_event
        case "UpdateUserFullNameEvent":
            update_user_fullname_event: UpdateUserFullNameEvent = UpdateUserFullNameEvent(**event.event_data)
            return update_user_fullname_event
        case "UpdateUserContactEvent":
            update_user_contact_event: UpdateUserContactEvent = UpdateUserContactEvent(**event.event_data)
            return update_user_contact_event
        case "DeleteUserEvent":
            delete_user_event: DeleteUserEvent = DeleteUserEvent(**event.event_data)
            return delete_user_event