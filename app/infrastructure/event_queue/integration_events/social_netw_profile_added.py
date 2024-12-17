from dataclasses import dataclass
from uuid import UUID

from app.domain.profile.events.social_netw_profile_added import SocialNetwProfileAdded as DomainEventSocialNetwProfileAdded
from app.infrastructure.event_queue.integration_events.integration_event import IntegrationEvent


@dataclass(frozen=True)
class SocialNetwProfileAdded(IntegrationEvent):
    profile_owner_id: UUID
    profile_id: UUID
    social_netw_profile_id: UUID
    social_netw_profile_type: str
    social_netw_profile_url: str


def social_netw_profile_added_to_integration(
    event: DomainEventSocialNetwProfileAdded,
) -> SocialNetwProfileAdded:
    return SocialNetwProfileAdded(
        event_id=event.event_uuid,
        event_type=event.event_type,
        occurred_at=event.occurred_at,
        profile_owner_id=event.profile_owner_id,
        profile_id=event.profile_id,
        social_netw_profile_id=event.social_netw_profile_id,
        social_netw_profile_type=event.social_netw_profile_type,
        social_netw_profile_url=event.social_netw_profile_url,
    )
