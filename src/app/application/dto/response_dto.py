from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.domain.value_objects.user_contact_value_object import UserContact
from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.domain.entities.user_entities import UserEntity


@dataclass(frozen=True)
class CreateUserResponse:
    uuid: UUID

    @staticmethod
    def from_entity(user_uuid: UserUUID) -> 'CreateUserResponse':
        return CreateUserResponse(
            uuid=user_uuid.to_raw(),
        )


@dataclass(frozen=True)
class GetUserResponse:
    uuid: UUID
    user_name: str
    user_contact: str
    user_created_at: datetime
    user_updated_at: datetime

    @staticmethod
    def from_entity(user: UserEntity) -> 'GetUserResponse':
        return GetUserResponse(
            uuid=user.uuid.to_raw(),
            user_name=user.user_name.to_raw(),
            user_contact=user.user_contact.to_raw(),
            user_created_at=user.user_created_at.to_raw(),
            user_updated_at=user.user_updated_at.to_raw(),
        )
    

@dataclass(frozen=True)
class UpdateUserContactResponse:
    new_user_contact: str

    @staticmethod
    def from_entity(user_contact: UserContact) -> 'UpdateUserContactResponse':
        return UpdateUserContactResponse(
            new_user_contact=user_contact.to_raw(),
        )
    

@dataclass(frozen=True)
class UpdateUserNameResponse:
    new_user_name: str

    @staticmethod
    def from_entity(user_name: UserName) -> 'UpdateUserNameResponse':
        return UpdateUserNameResponse(
            new_user_name=user_name.to_raw(),
        )
    
@dataclass(frozen=True)
class AuthentificationResponse:
    user_uuid: UUID

    @staticmethod
    def from_entity(user_uuid: UserUUID) -> 'AuthentificationResponse':
        return AuthentificationResponse(
            user_uuid=user_uuid.to_raw(),
        )