from dataclasses import dataclass
from typing import Self

from app.domain.common.common_domain_value_object import CommonDomainValueObject
from app.domain.user_profile.exceptions.user_profile_validation_errors import InvalidAddressException


@dataclass(frozen=True)
class AddressValueObject(CommonDomainValueObject):
    address: str | None

    def __post_init__(self: Self) -> None:
        if self.address:
            if not isinstance(self.address, str):
                raise InvalidAddressException(
                    message=f"Address must be a string, not {type(self.address)}",
                )
