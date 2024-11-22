from app.domain.common.common_domain_exception import CommonDomainException


class InvalidTimestampException(CommonDomainException):
    ...

class InvalidEmailException(CommonDomainException):
    ...

class InvalidPhoneNumberException(CommonDomainException):
    ...

class InvalidUserNameException(CommonDomainException):
    ...

class InvalidUuidException(CommonDomainException):
    ...

class InvalidContactConfiguration(CommonDomainException):
    ...
