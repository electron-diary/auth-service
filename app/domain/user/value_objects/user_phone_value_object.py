from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import InvalidPhoneNumberException


@dataclass(frozen=True)
class UserPhoneValueObject(CommonDomainValueObject[int | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), int):
                raise InvalidPhoneNumberException(
                    message=f"Phone number must be an integer, not {type(self.to_raw())}",
                )
            if len(str(self.to_raw())) < ...:
                raise InvalidPhoneNumberException(
                    message=f"Phone number must be larger than {...} characters",
                )
            if len(str(self.to_raw())) > ...:
                raise InvalidPhoneNumberException(
                    message=f"Phone number must be smaller than {...} characters",
                )
