from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.enums.bio_enums import BioEnums
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidBioException


@dataclass(frozen=True)
class BioValueObject(CommonDomainValueObject[str | None]):
    bio: str | None

    def __post_init__(self: Self) -> None:
        if self.bio:
            if not isinstance(self.bio, str):
                raise InvalidBioException(
                    message=f"Bio must be a string, not {type(self.bio)}",
                )
            if len(self.bio) > BioEnums.max_bio_characters:
                raise InvalidBioException(
                    message=f"Bio must be less than {BioEnums.max_bio_characters} characters",
                )
