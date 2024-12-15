from app.application.exception import ApplicationError


class UserAlreadyExistsError(ApplicationError):
    ...

class UserNotFoundError(ApplicationError):
    ...
