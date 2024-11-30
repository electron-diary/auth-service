from dataclasses import dataclass

from app.application.base.exception import ApplicationError


@dataclass
class UserNotFoundError(ApplicationError):
    ...

@dataclass
class UserAlreadyExistsError(ApplicationError):
    ...
