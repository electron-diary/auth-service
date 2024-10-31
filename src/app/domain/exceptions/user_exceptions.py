from app.domain.common.exceptions import DomainException


class UserNotFoundError(DomainException):
    pass

class UserAlreadyExistsError(DomainException):
    pass