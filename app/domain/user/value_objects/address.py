from typing import Self

from app.domain.user.exceptions import ErrorType, UserError


class Address:
    def __init__(
        self: Self,
        country: str | None = None,
        city: str | None = None,
        street: str | None = None,
        house_location: str | None = None,
    ) -> None:
        self.country: str | None = country
        self.city: str | None = city
        self.street: str | None = street
        self.house_location: int = house_location

        self.to_raw()

    def to_raw(self: Self) -> None:
        if self.country and not isinstance(self.country, str):
            raise UserError("Invalid country", ErrorType.INVALID_ADDRESS)

        if self.city and not isinstance(self.city, str):
            raise UserError("Invalid city", ErrorType.INVALID_ADDRESS)

        if self.street and not isinstance(self.street, str):
            raise UserError("Invalid street", ErrorType.INVALID_ADDRESS)

        if self.house_location and not isinstance(self.house_location, int):
            raise UserError("Invalid house location", ErrorType.INVALID_ADDRESS)

