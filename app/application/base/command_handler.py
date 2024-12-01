from abc import abstractmethod
from typing import Protocol, Self


class CommandHandler[Command, Response](Protocol):
    """
    Generic Protocol defining the interface for command handlers in the system.
    Implements the Command pattern and supports CQRS architecture.

    Type Parameters:
        Command: The type of command this handler processes
        Response: The type of response returned after command processing

    This Protocol defines the contract that all command handlers must follow,
    ensuring consistent command handling across the application.

    Usage:
        - Define specific command handlers
        - Process business operations
        - Handle state changes
        - Return operation results

    Example implementations:
        class CreateUserHandler(CommandHandler[CreateUserCommand, User]):
            async def __call__(self, command: CreateUserCommand) -> User:
                # Implementation

        class UpdateProfileHandler(CommandHandler[UpdateProfileCommand, None]):
            async def __call__(self, command: UpdateProfileCommand) -> None:
                # Implementation

    Note:
        - Handlers should be stateless
        - Each handler processes one specific command type
        - Handlers should encapsulate all command processing logic
        - Async implementation allows for I/O operations
    """

    @abstractmethod
    async def __call__(self: Self, command: Command) -> Response:
        """
        Process the given command and return appropriate response.

        Args:
            command (Command): The command to be processed

        Returns:
            Response: The result of command processing

        Raises:
            NotImplementedError: When the handler is not properly implemented
            Various domain exceptions based on business rules
        """
        raise NotImplementedError("method must be implemented by subclasses")
