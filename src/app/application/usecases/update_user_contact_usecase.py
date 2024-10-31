from typing import Self
from datetime import datetime
import logging
from logging import Logger

from app.application.dto.request_dto import UpdateUserContactRequest
from app.application.dto.response_dto import UpdateUserContactResponse
from app.domain.repositories.user_repository import UserRepositoryInterface
from app.application.interfaces.interactor import Interactor
from app.domain.value_objects.user_contact_value_object import UserContact
from app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from app.domain.value_objects.user_uuid_value_object import UserUUID
from app.application.interfaces.interactor import Interactor


logger: Logger = logging.getLogger(__name__)


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
        logger.info(f'new user contact is {request.user_contact} for user {request.user_uuid}')
        return UpdateUserContactResponse.from_entity(user_contact=new_user_contact)