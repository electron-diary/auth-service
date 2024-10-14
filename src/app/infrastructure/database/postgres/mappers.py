from src.app.infrastructure.database.postgres.models.user import UserModel
from src.app.domain.value_objects.user_contact_value_object import UserContact
from src.app.domain.value_objects.user_created_at_value_object import UserCreatedAt
from src.app.domain.value_objects.user_name_value_object import UserName
from src.app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.domain.entities.user_entities import UserEntity



def user_entity_to_model(user: UserEntity) -> UserModel:
    return UserModel(
        uuid=user.uuid.to_raw(),
        user_name=user.user_name.to_raw(),
        user_contact=user.user_contact.to_raw(),
        user_created_at=user.user_created_at.to_raw(),
        user_updated_at=user.user_updated_at.to_raw()
    )


def user_model_to_entity(user: UserModel) -> UserEntity:
    return UserEntity(
        uuid=UserUUID(user.uuid),
        user_name=UserName(user.user_name),
        user_contact=UserContact(user.user_contact),
        user_created_at=UserCreatedAt(user.user_created_at),
        user_updated_at=UserUpdatedAt(user.user_updated_at)
    )
