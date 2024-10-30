from typing import Self
from datetime import datetime
from uuid import UUID
import logging
from logging import Logger

from src.app.application.dto.request_dto import CreateUserRequest
from src.app.application.dto.response_dto import CreateUserResponse
from src.app.domain.value_objects.user_contact_value_object import UserContact
from src.app.domain.value_objects.user_created_at_value_object import UserCreatedAt
from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.domain.value_objects.user_status_value_object import UserStatus
from src.app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.domain.entities.user_entities import UserEntity
from src.app.application.interfaces.interactor import Interactor
from src.app.domain.repositories.user_repository import UserRepositoryInterface
from src.app.application.interfaces.uuid_generator import UUIDGeneratorInterface


class CreateUserUseCase(Interactor[CreateUserRequest, CreateUserResponse]):
    def __init__(
        self: Self, user_interface: UserRepositoryInterface, uuid_generator: UUIDGeneratorInterface
    ) -> None:
        self.user_interface: UserRepositoryInterface = user_interface
        self.uuid_generator: UUIDGeneratorInterface = uuid_generator

    async def __call__(self: Self, request: CreateUserRequest) -> CreateUserResponse:
        datetime_now: datetime = datetime.now()
        generated_uuid: UUID = self.uuid_generator.generate_uuid()

        user_uuid: UserUUID = await self.user_interface.create_user(
            user=UserEntity(
                uuid=UserUUID(generated_uuid),
                user_name=UserName(request.name),
                user_contact=UserContact(request.contact),              
                is_active=UserStatus(False),
                user_created_at=UserCreatedAt(datetime_now),
                user_updated_at=UserUpdatedAt(datetime_now)
            )
        )
        logging.info
        return CreateUserResponse.from_entity(user_uuid=user_uuid)
