from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.enums.user_email_enums import UserEmailEnums
from app.domain.user.enums.user_phone_enums import UserPhoneEnums
from app.domain.user.exceptions.user_validation_errors import (
    InvalidContactConfiguration,
    InvalidEmailException,
    InvalidPhoneNumberException,
)


@dataclass(frozen=True)
class UserContacts(CommonDomainValueObject):
    email: str | None
    phone: str | None

    def __post_init__(self: Self) -> None:
        if self.email:
            if not isinstance(self.email, str):
                raise InvalidEmailException(
                    message=f"Email must be a string, not {type(self.email)}",
                )
            if len(self.email) > UserEmailEnums.max_email_characters:
                raise InvalidEmailException(
                    message=f"Email must be smaller than {UserEmailEnums.max_email_characters} characters",
                )
            if len(self.email) < UserEmailEnums.min_email_characters:
                raise InvalidEmailException(
                    message=f"Email must be larger than {UserEmailEnums.min_email_characters} characters",
                )
        if self.phone:
            if not isinstance(self.phone, int):
                raise InvalidPhoneNumberException(
                    message=f"Phone number must be an integer, not {type(self.phone)}",
                )
            if len(str(self.phone)) < UserPhoneEnums.min_phone_number_cahracters:
                raise InvalidPhoneNumberException(
                    message=f"Phone number must be larger than {UserPhoneEnums.min_phone_number_cahracters} characters",
                )
            if len(str(self.phone)) > UserPhoneEnums.max_phone_number_cahracters:
                raise InvalidPhoneNumberException(
                    message=f"Phone number must be smaller than {UserPhoneEnums.max_phone_number_cahracters} characters",
                )
        if not self.email and not self.phone:
            raise InvalidContactConfiguration(
                message="User must have at least one contact configuration",
            )


