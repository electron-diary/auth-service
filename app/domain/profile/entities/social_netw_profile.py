from typing import Self
from uuid import UUID

from app.domain.unit_of_work import UnitOfWorkTrackerInterface
from app.domain.uowed import UowedEntity


class SocialNetwProfile(UowedEntity[UUID]):
    def __init__(
        self: Self,
        uow: UnitOfWorkTrackerInterface,
        social_netw_id: UUID,
        profile_id: UUID,
        social_profile_link: str,
        social_netw_name: str,
    ) -> None:
        super().__init__(uow, social_netw_id)

        self.social_profile_link = social_profile_link
        self.social_netw_name = social_netw_name
        self.profile_id = profile_id

    @classmethod
    def create_social_netw_profile(
        cls: type[Self],
        uow: UnitOfWorkTrackerInterface,
        social_netw_id: UUID,
        social_profile_link: str,
        profile_id: UUID,
        social_netw_name: str,
    ) -> Self:
        social_netw_profile = cls(
            uow=uow,
            profile_id=profile_id,
            social_netw_id=social_netw_id,
            social_profile_link=social_profile_link,
            social_netw_name=social_netw_name,
        )
        social_netw_profile.mark_new()

        return social_netw_profile

    def delete_social_netw_profile(self: Self) -> None:
        self.mark_deleted()
