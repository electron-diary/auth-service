from dataclasses import dataclass
from typing import Literal, Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidSocialProfileException

SocialProfilesT = Literal["vk", "tg", "inst", "fb", "tw", "ok"]


@dataclass(frozen=True)
class SocialProfilesValueObject(CommonDomainValueObject[dict[SocialProfilesT] | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), dict):
                raise InvalidSocialProfileException(
                    message=f"Social profiles must be a dictionary, not {type(self.to_raw())}",
                )
            for key, value in self.to_raw().items():
                if key not in ["vk", "tg", "inst", "fb", "tw", "ok"]:
                    raise InvalidSocialProfileException(
                        message="Social profiles must be either 'vk', 'tg', 'inst', 'fb', 'tw', 'ok'",
                    )
                if not isinstance(value, str):
                    raise InvalidSocialProfileException(
                        message="Social profiles links must be a string",
                    )
