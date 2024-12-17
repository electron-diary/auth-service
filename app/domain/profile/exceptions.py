from app.domain.common.exception import DomainError


class InvalidFullNameError(DomainError):
    ...

class ProfileInactiveError(DomainError):
    ...

class SocialNetwProfileNotFoundError(DomainError):
    ...

class AddressNotFoundError(DomainError):
    ...
