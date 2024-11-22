from dataclasses import dataclass
from typing import Any, Literal, Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidSocialProfileException

SocialProfilesT = Literal["vk", "tg", "inst", "fb", "tw", "ok"]


@dataclass(frozen=True)
class SocialProfilesValueObject(CommonDomainValueObject):
    social_profiles: dict[SocialProfilesT, Any] | None

    def __post_init__(self: Self) -> None:
        if self.social_profiles:
            if not isinstance(self.social_profiles, dict):
                raise InvalidSocialProfileException(
                    message=f"Social profiles must be a dictionary, not {type(self.social_profiles)}",
                )
            for key, value in self.social_profiles.items():
                if key not in ["vk", "tg", "inst", "fb", "tw", "ok"]:
                    raise InvalidSocialProfileException(
                        message="Social profiles must be either 'vk', 'tg', 'inst', 'fb', 'tw', 'ok'",
                    )
                if not isinstance(value, str):
                    raise InvalidSocialProfileException(
                        message="Social profiles links must be a string",
                    )
