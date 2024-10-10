from typing import Self
from datetime import datetime

from src.app.application.dto.request_dto import UpdateUserContactRequest
from src.app.application.dto.response_dto import UpdateUserContactResponse
from src.app.domain.user.repositories import UserInterface
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.user.value_objects import UserContact, UserUpdatedAt, UserUUID


class UpdateUserContactUseCase(Interactor[UpdateUserContactRequest, UpdateUserContactResponse]):
    def __init__(self: Self, user_interface: UserInterface) -> None:
        self.user_interface: UserInterface = user_interface

    async def __call__(self: Self, request: UpdateUserContactRequest) -> UpdateUserContactResponse:
        datetime_now: datetime = datetime.now()
        new_user_contact: UserContact = await self.user_interface.update_user_contact(
            user_uuid=UserUUID(request.user_uuid),
            user_contact=UserContact(request.user_contact),
            user_updated_at=UserUpdatedAt(datetime_now),
        )
        return UpdateUserContactResponse.from_entity(new_user_contact=new_user_contact)