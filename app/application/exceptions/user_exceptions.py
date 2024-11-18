from app.application.base.base_exception import BaseApplicationError


class UserAlreadyExistsError(BaseApplicationError):
    ...

class UserNotFoundError(BaseApplicationError):
    ...