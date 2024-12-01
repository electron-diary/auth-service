from dataclasses import dataclass

from app.domain.base.domain_exception import DomainException


@dataclass
class UserException(DomainException):
    """
    Base exception class for all user-related domain exceptions.
    
    This class extends DomainException to handle specific exceptions that occur
    within the user domain context. It can be used as a base class for more
    specific user-related exceptions such as:
    - Invalid username format
    - Invalid phone number format
    
    Usage:
        raise UserException(message="Invalid username format")
    
    Inherits:
        DomainException: Base exception class for all domain-specific exceptions
    """

