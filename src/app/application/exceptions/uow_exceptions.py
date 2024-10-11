from src.app.domain.common.exceptions import DomainException

class UoWCommitError(DomainException):
    pass

class UoWRollbackError(DomainException):
    pass