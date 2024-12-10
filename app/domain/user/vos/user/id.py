from typing import Self
from uuid import UUID


class Id:
    def __init__(
        self: Self,
        value: UUID,
    ) -> None:
        self.value: UUID = value

        self.validate()

    def validate(self: Self) -> None:
        if not self.value:
            raise ValueError("Id cannot be empty")

        if not isinstance(self.value, UUID):
            raise ValueError("Id must be a UUID")
