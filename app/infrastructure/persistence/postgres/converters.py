from app.application.user.dto import UserDTO
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username
from app.infrastructure.persistence.postgres.tables import UserTable


def user_entity_to_table(user: User) -> UserTable:
    return UserTable(
        id=user.id.value,
        username=user.username.value,
        email=user.contacts.email,
        phone_number=user.contacts.phone,
        is_deleted=user.is_deleted.value,
    )

def table_to_user_entity(user: UserTable) -> User:
    return User(
        id=UserId(value=user.id),
        username=Username(value=user.username),
        contacts=Contacts(email=user.email, phone=user.phone_number),
        is_deleted=DeletedUser(value=user.is_deleted),
    )

def table_to_dto(user: UserTable) -> UserDTO:
    return UserDTO(
        id=user.id,
        username=user.username,
        email=user.email,
        phone=user.phone_number,
        is_deleted=user.is_deleted,
    )
