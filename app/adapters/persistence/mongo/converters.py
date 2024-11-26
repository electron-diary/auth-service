from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User


def events_to_user(events: list[DomainEvent]) -> User:
    ...