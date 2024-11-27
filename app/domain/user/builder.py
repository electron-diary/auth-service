from app.domain.user.actions import UserCreated
from app.domain.user.exceptions import UserException
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, DeletedUser, UserId, Username


class UserBuilder:
    @staticmethod
    def create_user(
        id: UserId, username: Username, contacts: Contacts, is_deleted: DeletedUser
    ) -> User:
        if contacts.email is None and contacts.phone is None:
            raise UserException("At least one contact (email or phone) must be provided.")
        user: User = User(
            id=id, username=username, contacts=contacts, is_deleted=is_deleted.value
        )
        action: UserCreated = UserCreated(
            user_id=id.value, username=username.value, email=contacts.email,
            phone_number=contacts.phone, is_deleted=is_deleted.value
        )
        user._add_action(action=action)
        return user
