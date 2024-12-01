from abc import abstractmethod
from typing import Protocol, Self

from app.domain.base.domain_event import DomainEvent


class EventHandler[Event: DomainEvent](Protocol):
    """
    Generic Protocol defining the interface for domain event handlers.
    Implements the Observer pattern for handling domain events.

    Type Parameters:
        Event: The specific type of DomainEvent this handler processes.
               Must be a subclass of DomainEvent.

    This Protocol defines the contract that all event handlers must follow,
    ensuring consistent event handling across the application.

    Usage:
        - Define specific event handlers
        - Process domain events asynchronously
        - Implement side effects of domain operations
        - Handle cross-aggregate consistency

    Example implementations:
        class UserCreatedEventHandler(EventHandler[UserCreatedEvent]):
            async def __call__(self, event: UserCreatedEvent) -> None:
                # Send welcome email
                # Initialize user preferences
                # etc.

        class OrderPlacedEventHandler(EventHandler[OrderPlacedEvent]):
            async def __call__(self, event: OrderPlacedEvent) -> None:
                # Update inventory
                # Notify shipping service
                # etc.

    Note:
        - Handlers should be stateless
        - Each handler processes one specific event type
        - Handlers should be idempotent when possible
        - Async implementation allows for I/O operations
    """

    @abstractmethod
    async def __call__(self: Self, event: Event) -> None:
        """
        Process the given domain event.

        Args:
            event (Event): The domain event to be handled

        Returns:
            None: Event handlers don't return values as they handle side effects

        Raises:
            NotImplementedError: When the handler is not properly implemented
            Various domain exceptions based on business rules
        """
        raise NotImplementedError("method must be implemented by subclasses")
