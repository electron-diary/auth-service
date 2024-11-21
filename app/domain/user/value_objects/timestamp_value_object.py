from typing import Self
from dataclasses import dataclass
from datetime import datetime

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user.exceptions.user_validation_errors import TimeStampRequiredException
from app.domain.user.exceptions.user_validation_errors import TimeStampInvalidException


@dataclass(frozen=True)
class TimestampValueObject(CommonDomainValueObject[datetime]):
    def __post_init__(self: Self) -> None:
        if not self.to_raw():
            raise TimeStampRequiredException(
                message='Timestamp object must be datetime, not None'
            )
        if not isinstance(self.to_raw(), datetime):
            raise TimeStampInvalidException(
                message=f'Timestamp object must be datetime, not {type(self.to_raw())}'
            )