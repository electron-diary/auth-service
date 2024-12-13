from app.domain.exception import DomainException


class InvalidContactsError(DomainException):
    ...

class UserInactiveError(DomainException):
    ...
