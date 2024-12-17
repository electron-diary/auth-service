from typing import Self


class DomainError(Exception):
    def __init__(
        self: Self,
        message: str,
    ) -> None:
        super().__init__(message)

        self.message = message
