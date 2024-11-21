from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import InvalidEmailException
from app.domain.user.enums.user_email_enums import UserEmailEnums


@dataclass(frozen=True)
class UserEmailValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise InvalidEmailException(
                    message=f"Email must be a string, not {type(self.to_raw())}",
                )
            if len(self.to_raw()) > UserEmailEnums.max_email_characters:
                raise InvalidEmailException(
                    message=f"Email must be smaller than {UserEmailEnums.max_email_characters} characters",
                )
            if len(self.to_raw()) < UserEmailEnums.min_email_characters:
                raise InvalidEmailException(
                    message=f"Email must be larger than {UserEmailEnums.min_email_characters} characters",
                )
