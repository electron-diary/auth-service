from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class DomainEvent:
    """
    Base class for all domain events in the system.
    Implements immutable event objects that represent state changes in the domain.

    This class provides the fundamental structure for domain events following
    Domain-Driven Design principles and event sourcing pattern.

    Attributes:
        agregate_id (UUID): The unique identifier of the aggregate root
            that this event belongs to or affects. Used for event sourcing
            and maintaining aggregate consistency.

        agregate_name (str): The name of the aggregate type (e.g., "User", "Order")
            that this event is associated with. Useful for event handling
            and routing.

        event_name (str): The name of the event describing what occurred
            (e.g., "UserCreated", "OrderPlaced"). Used for event
            identification and handling.
    """

    agregate_id: UUID
    agregate_name: str
    event_name: str
