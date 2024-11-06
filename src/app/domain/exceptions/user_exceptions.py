from app.domain.common.common_exceptions import CommonDomainError


class UserAlreadyExistsError(CommonDomainError):
    ...

class UserNotFoundError(CommonDomainError):
    ...
