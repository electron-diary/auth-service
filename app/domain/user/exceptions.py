from dataclasses import dataclass

from app.domain.base.domain_exception import DomainException

@dataclass
class UserException(DomainException):
    ...
