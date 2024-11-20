from typing import Self, Literal
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject

SocialProfilesT = Literal['vk', 'tg', 'inst', 'fb', 'tw', 'ok']


@dataclass(frozen=True)
class SocialProfilesValueObject(CommonDomainValueObject[dict[SocialProfilesT], str] | None):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), dict):
                raise ...
            for key, value in self.to_raw().items():
                if not isinstance(key, str):
                    raise ...
                if not isinstance(value, str):
                    raise ...
                if key not in ['vk', 'tg', 'inst', 'fb', 'tw', 'ok']:
                    raise ...