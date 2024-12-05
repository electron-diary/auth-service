from dataclasses import dataclass
from uuid import UUID

from app.domain.domain_event import DomainEvent


@dataclass(frozen=True)
class UserCreated(DomainEvent):
    user_id: UUID
    status: str
    phone_number: int | None
    email: str | None
    profile_id: UUID
    age: int | None
    gender: str | None
    first_name: str
    last_name: str
    middle_name: str | None
    country: str | None
    city: str | None
    street: str | None
    house_location: str | None
    pictures: list[str]