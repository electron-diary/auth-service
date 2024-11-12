from dataclasses import dataclass
from typing import Self

from app.domain.exceptions.value_objects_exceptions import MiddleNameTypeError
from app.domain.exceptions.value_objects_exceptions import MinimalLenghtMiddleNameError
from app.domain.exceptions.value_objects_exceptions import MaximalLenghtMiddleNameError
from app.domain.common.common_value_object import CommonDomainValueObject
from app.domain.enums.user_fullname_enum import UserFullnameEnums


@dataclass(frozen=True)
class UserMiddleNameValueObject(CommonDomainValueObject[str | None]):
    def __post_init__(self: Self) -> None:
        if self.to_raw():
            if not isinstance(self.to_raw(), str):
                raise MiddleNameTypeError(
                    f"User middle name must be a string get {type(self.to_raw())}",
                )
            if len(self.to_raw()) < UserFullnameEnums.user_middle_name_min_length:
                raise MinimalLenghtMiddleNameError(
                    f"User middle name must be at least {UserFullnameEnums.user_middle_name_min_length} characters long",
                )
            if len(self.to_raw()) > UserFullnameEnums.user_middle_name_max_lenght:
                raise MaximalLenghtMiddleNameError(
                    f"User middle name must be less than {UserFullnameEnums.user_middle_name_max_lenght} characters long",
                )
