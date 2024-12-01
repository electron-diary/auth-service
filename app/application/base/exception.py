from dataclasses import dataclass


@dataclass
class ApplicationError(Exception):
    """
    Base exception class for all application-layer errors.
    Extends the built-in Exception class to provide application-specific error handling.

    This class serves as the foundation for exceptions that occur in the application
    layer, distinguishing them from domain exceptions and infrastructure errors.

    Attributes:
        message (str): A descriptive message explaining the application error.
            Should provide clear, application-level context about what went wrong.

    Usage:
        - Base class for more specific application exceptions
        - Handling application-level errors
        - Distinguishing from domain and infrastructure errors
        - Providing meaningful error context

    Example uses:
        raise ApplicationError("Failed to process user registration")
        raise ApplicationError("Invalid query parameters")
        raise ApplicationError("Command handler not found")

    Note:
        - Should be used for application-specific errors only
        - Distinct from DomainException which handles business rule violations
        - Provides clear separation of concerns in error handling
    """

    message: str
