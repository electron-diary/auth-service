from app.domain.common.exception import DomainException


class InvalidContactsError(DomainException):
    ...

class UserInactiveError(DomainException):
    ...
