from dataclasses import dataclass


@dataclass(eq=False)
class ApplicationError(Exception):
    message: str


class ProfileNotFoundError(ApplicationError):
    ...


class UserAlreadyExistsError(ApplicationError):
    ...


class UserNotFoundError(ApplicationError):
    ...
