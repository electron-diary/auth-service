from src.app.domain.common.exceptions import DomainException

class AuthentificationError(DomainException):
    pass

class AccessDeniedError(DomainException):
    pass