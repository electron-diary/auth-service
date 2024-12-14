from app.application.exception import ApplicationError


class UserAlreadyExists(ApplicationError):
    ...

class UserNotFound(ApplicationError):
    ...
