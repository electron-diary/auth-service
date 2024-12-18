from app.domain.common.domain_event import DomainEvent
from app.domain.profile.events.address_added import AddressAdded
from app.domain.profile.events.address_deleted import AddressDeleted
from app.domain.profile.events.bio_changed import BioChanged
from app.domain.profile.events.fullname_changed import FullnameChanged
from app.domain.profile.events.profile_created import ProfileCreated
from app.domain.profile.events.profile_deleted import ProfileDeleted
from app.domain.profile.events.social_netw_profile_added import SocialNetwProfileAdded
from app.domain.profile.events.social_netw_profile_deleted import SocialNetwProfileDeleted
from app.domain.user.events.contacts_changed import ContactsChanged
from app.domain.user.events.user_created import UserCreated
from app.domain.user.events.user_deleted import UserDeleted
from app.domain.user.events.username_changed import UsernameChanged
from app.infrastructure.brokers.message import Message
from app.infrastructure.common.serializers import to_json
from app.infrastructure.event_queue.integration_events.address_added import address_added_to_integration
from app.infrastructure.event_queue.integration_events.address_deleted import address_deleted_to_integration
from app.infrastructure.event_queue.integration_events.bio_changed import bio_changed_to_integration
from app.infrastructure.event_queue.integration_events.contacts_changed import contacts_changed_to_integration
from app.infrastructure.event_queue.integration_events.fullname_changed import fullname_changed_to_integration
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent
from app.infrastructure.event_queue.integration_events.profile_created import profile_created_to_integration
from app.infrastructure.event_queue.integration_events.profile_deleted import profile_deleted_to_integration
from app.infrastructure.event_queue.integration_events.social_netw_profile_added import social_netw_profile_added_to_integration
from app.infrastructure.event_queue.integration_events.social_netw_profile_deleted import (
    social_netw_profile_deleted_to_integration,
)
from app.infrastructure.event_queue.integration_events.user_created import user_created_to_integration
from app.infrastructure.event_queue.integration_events.user_deleted import user_deleted_to_integration
from app.infrastructure.event_queue.integration_events.username_changed import username_changed_to_integration


def domain_event_to_integration_event(event: DomainEvent) -> IntegrationEvent:
    match event:
        case AddressAdded():
            return address_added_to_integration(event)
        case AddressDeleted():
            return address_deleted_to_integration(event)
        case BioChanged():
            return bio_changed_to_integration(event)
        case ContactsChanged():
            return contacts_changed_to_integration(event)
        case FullnameChanged():
            return fullname_changed_to_integration(event)
        case ProfileCreated():
            return profile_created_to_integration(event)
        case ProfileDeleted():
            return profile_deleted_to_integration(event)
        case SocialNetwProfileAdded():
            return social_netw_profile_added_to_integration(event)
        case SocialNetwProfileDeleted():
            return social_netw_profile_deleted_to_integration(event)
        case UserCreated():
            return user_created_to_integration(event)
        case UserDeleted():
            return user_deleted_to_integration(event)
        case UsernameChanged():
            return username_changed_to_integration(event)
        case _:
            raise ValueError(f"Unknown event type: {event}")


def integration_event_to_message(event: IntegrationEvent) -> Message:
    return Message(
        message_id=event.event_id,
        data=to_json(event),
    )
