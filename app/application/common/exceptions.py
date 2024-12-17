from typing import Self


class ApplicationError(Exception):
    def __init__(self: Self, message: str) -> None:
        super().__init__(message)

        self.message = message


class ProfileNotFoundError(ApplicationError):
    ...


class UserAlreadyExistsError(ApplicationError):
    ...


class UserNotFoundError(ApplicationError):
    ...
