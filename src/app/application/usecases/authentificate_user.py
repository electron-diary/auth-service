from typing import Self
from datetime import datetime
from uuid import UUID
import logging
from logging import Logger

from app.application.dto.request_dto import AuthentificateUserRequest
from app.application.dto.response_dto import AuthentificationResponse
from app.application.interfaces.interactor import Interactor
from app.domain.repositories.user_repository import UserRepositoryInterface
from app.application.interfaces.user_name_generator import UserNameGeneratorInterface
from app.domain.value_objects.user_uuid_value_object import UserUUID
from app.domain.value_objects.user_contact_value_object import UserContact
from app.domain.value_objects.user_name_value_object import UserName
from app.domain.value_objects.user_created_at_value_object import UserCreatedAt
from app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from app.application.interfaces.uuid_generator import UUIDGeneratorInterface
from app.domain.value_objects.user_status_value_object import UserStatus
from app.domain.entities.user_entities import UserEntity
from app.domain.value_objects.user_uuid_value_object import UserUUID


logger: Logger = logging.getLogger(__name__)


class AuthentificateUserUseCase(Interactor[AuthentificateUserRequest, AuthentificationResponse]):
    def __init__(
        self: Self, user_repository: UserRepositoryInterface,
        user_name_generator: UserNameGeneratorInterface,
        uuid_generator: UUIDGeneratorInterface
    ) -> None:
        self.user_repository: UserRepositoryInterface = user_repository
        self.user_name_generator: UserNameGeneratorInterface = user_name_generator
        self.uuid_generator: UUIDGeneratorInterface = uuid_generator
   
    async def __call__(self: Self, request: AuthentificateUserRequest) -> AuthentificationResponse:
        user_uuid: UserUUID = await self.user_repository.get_user_uuid_by_contact(
            user_contact=UserContact(object=request.user_contact)
        )
        user_status: UserStatus = UserStatus(False)
        if not user_uuid:
            time_now: datetime = datetime.now()
            user_name: str = self.user_name_generator.generate_user_name()
            generated_uuid: UUID = self.uuid_generator.generate_uuid()

            user_uuid: UserUUID = await self.user_repository.create_user(
                user=UserEntity(
                    uuid=UserUUID(generated_uuid),
                    user_name=UserName(user_name),
                    user_contact=UserContact(request.user_contact),
                    user_created_at=UserCreatedAt(time_now),
                    user_updated_at=UserUpdatedAt(time_now),
                    is_active=user_status
                )
            )
        logger.info(f"User {user_uuid.to_raw()} authentificated, confirmation-code sended")
        return AuthentificationResponse.from_entity(user_uuid=user_uuid, user_status=user_status)
        
        