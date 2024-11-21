from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import InvalidUserEmailException
from app.domain.user.exceptions.user_validation_errors import EmailSmallerThanAllowedException
from app.domain.user.exceptions.user_validation_errors import EmailLargerThanAllowedException


@dataclass(frozen=True)
class UserEmailValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise InvalidUserEmailException(
                    message=f"Email must be a string, not {type(self.to_raw())}"
                )
            if len(self.to_raw()) > ...:
                raise EmailLargerThanAllowedException(
                    message=f"Email must be smaller than {...} characters"
                )
            if len(self.to_raw()) < ...:
                raise EmailSmallerThanAllowedException(
                    message=f"Email must be larger than {...} characters"
                )