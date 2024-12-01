from dataclasses import dataclass


@dataclass
class DomainEntity[EntityId]:
    """
    Generic base class for all domain entities in the system.
    Uses generic type parameter for flexible ID types.

    This class serves as the foundation for all entities in the domain model,
    providing identity characteristics through a generic ID field.

    Type Parameters:
        EntityId: The type of the identifier (e.g., UUID, int, str)
            Used to make the class flexible for different ID types

    Attributes:
        id (EntityId): The unique identifier for the entity
            The actual type depends on the EntityId type parameter
    """

    id: EntityId
