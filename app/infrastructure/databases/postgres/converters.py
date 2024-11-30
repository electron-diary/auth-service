from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username
from app.infrastructure.databases.postgres.tables import UserTable


def convert_user_table_to_user(user_table: UserTable) -> User:
    return User(
        id=UserId(user_table.id),
        username=Username(user_table.username),
        contacts=Contacts(user_table.phone_number),
        is_deleted=DeletedUser(user_table.is_deleted),
    )

def convert_user_to_table(user: User) -> UserTable:
    return UserTable(
        id=user.id.value,
        username=user.username.value,
        phone_number=user.contacts.phone,
        is_deleted=user.is_deleted.value,
    )
