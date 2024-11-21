from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import InvalidUserNameException
from app.domain.user.enums.username_enums import UsernameEnums


@dataclass(frozen=True)
class UserNameValueObject(CommonDomainValueObject[str]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise InvalidUserNameException(
                message="Username object must be string, not None",
            )
        if not isinstance(self.to_raw(), str):
            raise InvalidUserNameException(
                message=f"Username object must be string, not {type(self.to_raw())}",
            )
        if len(self.to_raw()) < UsernameEnums.min_username_characters:
            raise InvalidUserNameException(
                message=f"Username object must be larger than {UsernameEnums.min_username_characters} characters",
            )
        if len(self.to_raw()) > UsernameEnums.max_username_characters:
            raise InvalidUserNameException(
                message=f"Username object must be smaller than {UsernameEnums.max_username_characters} characters",
            )
