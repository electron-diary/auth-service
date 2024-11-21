from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidInterestsException


@dataclass(frozen=True)
class InterestsValueObject(CommonDomainValueObject[list[str] | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), list):
                raise InvalidInterestsException(
                    message=f"Interests must be a list of strings, not {type(self.to_raw())}",
                )
            if len(self.to_raw()) > ...:
                raise InvalidInterestsException(
                    message=f"Interests must be less than {...} items",
                )
            for interest in self.to_raw():
                if not isinstance(interest, str):
                    raise InvalidInterestsException(
                        message=f"Each interest must be a string, not {type(interest)}",
                    )
