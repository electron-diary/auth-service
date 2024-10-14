from typing import Self
from datetime import datetime

from src.app.application.dto.request_dto import UpdateUserContactRequest
from src.app.application.dto.response_dto import UpdateUserContactResponse
from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.value_objects.user_contact_value_object import UserContact
from src.app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.application.interfaces.interactor import Interactor


class UpdateUserContactUseCase(Interactor[UpdateUserContactRequest, UpdateUserContactResponse]):
    def __init__(self: Self, user_interface: UserRepositoryInterface) -> None:
        self.user_interface: UserRepositoryInterface = user_interface

    async def __call__(self: Self, request: UpdateUserContactRequest) -> UpdateUserContactResponse:
        datetime_now: datetime = datetime.now()
        new_user_contact: UserContact = await self.user_interface.update_user_contact(
            user_uuid=UserUUID(request.user_uuid),
            user_contact=UserContact(request.user_contact),
            user_updated_at=UserUpdatedAt(datetime_now),
        )
        return UpdateUserContactResponse.from_entity(user_contact=new_user_contact)