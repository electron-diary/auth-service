from app.domain.base.domain_event import DomainEvent
from app.domain.user.user import User
from app.domain.user.actions import UserCreated
from app.domain.user.value_objects import UserId, Username, Contacts, DeleteDate, CreatedDate


def events_to_user(events: list[DomainEvent]) -> User:
    user_created: UserCreated = events[0]
    user: User = User(
        id=UserId(user_created.user_id),
        username=Username(user_created.username),
        contacts=Contacts(email=user_created.email, phone=user_created.phone_number),
        created_at=CreatedDate(user_created.created_at),
        delete_date=DeleteDate(user_created.updated_at),
    )
    for event in events[1:]:
        user._apply(action=event)
    
    return user
