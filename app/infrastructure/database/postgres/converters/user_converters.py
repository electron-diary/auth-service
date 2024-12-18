from app.application.dto.user_dto import UserDto
from app.domain.common.unit_of_work import UnitOfWorkTracker
from app.domain.user.entities.user import User
from app.domain.user.value_objects.contacts import Contacts


def result_to_dto(result: dict) -> UserDto:
    return UserDto(
        user_id=result["user_id"],
        email=result["email"],
        phone_number=result["phone_number"],
        username=result["username"],
        status=result["status"],
    )

def result_to_user_entity(result: dict, uow: UnitOfWorkTracker) -> User:
    return User(
        uow=uow,
        user_id=result["user_id"],
        contacts=Contacts(
            email=result["email"],
            phone_number=result["phone_number"],
        ),
        username=result["username"],
        status=result["status"],
    )
