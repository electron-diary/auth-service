from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidBioException
from app.domain.user_profile.enums.bio_enums import BioEnums


@dataclass(frozen=True)
class BioValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise InvalidBioException(
                    message=f"Bio must be a string, not {type(self.to_raw())}",
                )
            if len(self.to_raw()) > BioEnums.max_bio_characters:
                raise InvalidBioException(
                    message=f"Bio must be less than {BioEnums.max_bio_characters} characters",
                )
