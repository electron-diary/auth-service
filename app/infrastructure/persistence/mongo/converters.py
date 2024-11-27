from app.domain.base.domain_event import DomainEvent
from app.domain.user.actions import UserCreated
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


def events_to_user(events: list[DomainEvent]) -> User:
    print(events)
    user_created: UserCreated = events[0]
    user: User = User(
        id=UserId(user_created.user_id),
        username=Username(user_created.username),
        contacts=Contacts(email=user_created.email, phone=user_created.phone_number),
        is_deleted=DeletedUser(user_created.is_deleted),
    )
    for event in events[1:]:
        user._apply(action=event)

    return user
