from dataclasses import dataclass


@dataclass(frozen=True)
class BaseCommand:
    """
    Base class for all command objects in the system following Command pattern.
    Implements immutable command structure for handling business operations.

    This class serves as the foundation for all commands that represent
    intentions to change the system state. Commands are immutable to ensure
    integrity during processing.

    Usage:
        - Base class for specific command implementations
        - Represents intent to perform domain operations
        - Part of Command Query Responsibility Segregation (CQRS) pattern
        - Enables command validation and handling

    Example command implementations:
        - CreateUserCommand
        - UpdateProfileCommand
        - DeleteAccountCommand
        - ProcessPaymentCommand

    Note:
        Commands should be named in imperative form and represent a single action
        The frozen=True decorator ensures commands are immutable once created
    """

