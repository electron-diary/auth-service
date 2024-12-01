from dataclasses import dataclass


@dataclass
class DomainException(Exception):
    """
    Base exception class for all domain-specific exceptions in the system.
    Extends the built-in Exception class to provide domain-specific error handling.

    This class serves as the foundation for all custom exceptions that represent
    business rule violations or invalid operations within the domain model.

    Attributes:
        message (str): A descriptive message explaining why the exception occurred.
            Should provide clear, business-oriented explanation of the error.

    Usage:
        - Base class for more specific domain exceptions
        - Capturing business rule violations
        - Handling domain-specific error cases
        - Providing meaningful error messages

    Example:
        raise DomainException("Invalid user state for this operation")
    """

    message: str
