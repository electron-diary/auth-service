from dataclasses import dataclass
from typing import Self

from app.domain.common.common_exceptions import DomainValidationError
from app.domain.common.common_value_object import CommonDomainValueObject
from app.domain.enums.user_contact_enum import UserContactEnums


@dataclass(frozen=True)
class UserEmailValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise DomainValidationError(
                    f"User email must be a string, get {type(self.to_raw())}",
                )
            if len(self.to_raw()) < UserContactEnums.user_email_min_lenght:
                raise DomainValidationError(
                    f"User email must be at least {UserContactEnums.user_email_min_lenght} characters long",
                )
            if len(self.to_raw()) > UserContactEnums.user_email_max_lenght:
                raise DomainValidationError(
                    f"User email must be less than {UserContactEnums.user_email_max_lenght} characters long",
                )

