from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidInterestsException


@dataclass(frozen=True)
class InterestsValueObject(CommonDomainValueObject):
    interests: list[str] | None

    def __post_init__(self: Self) -> None:
        if self.interests:
            if not isinstance(self.interests, list):
                raise InvalidInterestsException(
                    message=f"Interests must be a list of strings, not {type(self.interests)}",
                )
            for interest in self.interests:
                if not isinstance(interest, str):
                    raise InvalidInterestsException(
                        message=f"Each interest must be a string, not {type(interest)}",
                    )
