from dataclasses import dataclass
from datetime import datetime
from typing import Self

from app.domain.exceptions.value_objects_exceptions import TimestampTypeError
from app.domain.exceptions.value_objects_exceptions import TimestampRequiredError
from app.domain.common.common_value_object import CommonDomainValueObject


@dataclass(frozen=True)
class TimestampValueObject(CommonDomainValueObject[datetime]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise TimestampRequiredError(
                "User updated at cannot be empty",
            )
        if not isinstance(self.to_raw(), datetime):
            raise TimestampTypeError(
                f"User updated at must be a datetime, get {type(self.to_raw())}",
            )
