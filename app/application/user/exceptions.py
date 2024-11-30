from app.application.base.exception import ApplicationError


class UserNotFoundError(ApplicationError):
    ...

class UserAlreadyExistsError(ApplicationError):
    ...
