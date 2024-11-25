from app.domain.user.actions import UserCreated
from app.domain.user.exceptions import UserException
from app.domain.user.user import User
from app.domain.user.value_objects import Contacts, CreatedDate, DeleteDate, UserId, Username


class UserBuilder:
    @staticmethod
    def create_user(
        id: UserId, username: Username, contacts: Contacts, delete_date: DeleteDate, created_date: CreatedDate,
    ) -> User:
        if contacts.email is None and contacts.phone is None:
            raise UserException("At least one contact (email or phone) must be provided.")
        user: User = User(
            id=id, username=username, contacts=contacts, delete_date=delete_date,created_date=created_date,
        )
        action: UserCreated = UserCreated(
            user_id=id, username=username, email=contacts.email,
            phone_number=contacts.phone, created_at=created_date, deleted_date=delete_date,
        )
        user._apply(action=action)
        return user
