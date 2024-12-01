from dataclasses import dataclass, field
from typing import Self

from app.domain.base.domain_event import DomainEvent


@dataclass
class AgregateRoot:
    """
    Base class for aggregate roots in the domain model.
    Implements event tracking functionality for domain events.
    
    An aggregate root is an entity that encapsulates and ensures consistency
    for a cluster of domain objects. It tracks all domain events that occur
    within its aggregate boundary.

    Attributes:
        _events (list[DomainEvent]): Private list storing domain events that occurred
            in this aggregate. Initialized as empty list and not exposed in constructor.
    """

    _events: list[DomainEvent] = field(default_factory=list, init=False)

    def _add_event(self: Self, event: DomainEvent) -> None:
        """
        Records a new domain event in the aggregate's event list.
        
        This method is called internally when state-changing operations occur
        within the aggregate.

        Args:
            event (DomainEvent): The domain event to be recorded
        """
        self._events.append(event)

    def get_events(self: Self) -> list[DomainEvent]:
        """
        Retrieves and clears all recorded events from this aggregate.
        
        This method is typically called by the infrastructure layer to process
        all pending events (e.g., for event sourcing or publishing to event bus).

        Returns:
            list[DomainEvent]: A copy of all recorded events

        Note:
            This method clears the internal event list after returning the events,
            ensuring events are processed only once.
        """
        actions: list[DomainEvent] = self._events.copy()
        self._events.clear()
        return actions
