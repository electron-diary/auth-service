from app.domain.common.exception import DomainException


class InvalidFullNameError(DomainException):
    ...

class ProfileInactiveError(DomainException):
    ...

class SocialNetwProfileNotFoundError(DomainException):
    ...

class AddressNotFoundError(DomainException):
    ...
