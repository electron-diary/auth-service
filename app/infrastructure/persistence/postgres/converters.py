from app.application.user.dto import UserDTO
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, CreatedDate, DeleteDate, UserId, Username
from app.infrastructure.persistence.postgres.tables import UserTable


def user_entity_to_table(user: User) -> UserTable:
    return UserTable(
        id=user.id.value,
        username=user.username.value,
        email=user.contacts.email,
        phone_number=user.contacts.phone,
        delete_date=user.delete_date.value,
        created_date=user.created_at.value,
    )

def table_to_user_entity(user: UserTable) -> User:
    return User(
        id=UserId(value=user.id),
        username=Username(value=user.username),
        contacts=Contacts(email=user.email, phone=user.phone_number),
        delete_date=DeleteDate(value=user.delete_date),
        created_at=CreatedDate(value=user.created_date),
    )

def table_to_dto(user: UserTable) -> UserDTO:
    return UserDTO(
        id=user.id,
        username=user.username,
        email=user.email,
        phone=user.phone_number,
        delete_date=user.delete_date,
        created_at=user.created_date,
    )
