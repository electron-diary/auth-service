from dataclasses import dataclass
from typing import Self

from app.domain.value_objects.user_phone_value_object import UserPhoneValueObject
from app.domain.value_objects.user_email_value_object import UserEmailValueObject
from app.domain.common.common_exceptions import DomainValidationError


@dataclass(frozen=True)
class UserContact:
    user_email: UserEmailValueObject
    user_phone: UserPhoneValueObject

    def __post_init__(self: Self) -> None:
        if not self.user_email.to_raw() and not self.user_phone.to_raw():
            raise DomainValidationError("At least one of user_email or user_phone must be provided.")

    