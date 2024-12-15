from app.application.user.dtos.user_dto import UserDto
from app.domain.unit_of_work import UnitOfWorkTrackerInterface
from app.domain.user.entities.user import User
from app.domain.user.vos.contacts import Contacts


def result_to_dto(result: dict) -> UserDto:
    return UserDto(
        user_id=result["user_id"],
        email=result["email"],
        phone_number=result["phone_number"],
        username=result["username"],
        status=result["status"],
    )

def result_to_user_entity(result: dict, uow: UnitOfWorkTrackerInterface) -> User:
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
