from typing import Self
from dataclasses import dataclass

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import UserNameRequiredException
from app.domain.user.exceptions.user_validation_errors import UserNameLargerThanAllowedException
from app.domain.user.exceptions.user_validation_errors import UserNameSmallerThanAllowedException
from app.domain.user.exceptions.user_validation_errors import InvalidUserNameException


@dataclass(frozen=True)
class UserNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise UserNameRequiredException(
                message='Username object must be string, not None'
            )
        if not isinstance(self.to_raw(), str):
            raise InvalidUserNameException(
                message=f'Username object must be string, not {type(self.to_raw())}'
            )
        if len(self.to_raw()) < ...:
            raise UserNameSmallerThanAllowedException(
                message=f'Username object must be larger than {...} characters'
            )
        if len(self.to_raw()) > ...:
            raise UserNameLargerThanAllowedException(
                message=f'Username object must be smaller than {...} characters'
            )