from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.social_netw_profile_deleted import SocialNetwProfileDeleted as DomainEventSocialNetwProfileDeleted
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class SocialNetwProfileDeleted(IntegrationEvent):
    profile_owner_id: UUID
    profile_id: UUID
    social_netw_profile_id: UUID


def social_netw_profile_deleted_to_integration(
    event: DomainEventSocialNetwProfileDeleted,
) -> SocialNetwProfileDeleted:
    return SocialNetwProfileDeleted(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_owner_id=event.profile_owner_id,
        profile_id=event.profile_id,
        social_netw_profile_id=event.social_netw_profile_id,
    )
