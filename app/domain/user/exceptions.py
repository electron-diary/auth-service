from app.domain.common.exception import DomainError


class InvalidContactsError(DomainError):
    ...

class UserInactiveError(DomainError):
    ...
