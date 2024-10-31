from typing import Self
from uuid import UUID
from sqlalchemy import select, update, delete, insert
from sqlalchemy.exc import IntegrityError

from app.domain.entities.user_entities import UserEntity
from app.domain.value_objects.user_status_value_object import UserStatus
from app.domain.value_objects.user_contact_value_object import UserContact
from app.domain.value_objects.user_created_at_value_object import UserCreatedAt
from app.domain.value_objects.user_name_value_object import UserName
from app.domain.value_objects.user_updated_at_value_object import UserUpdatedAt
from app.domain.value_objects.user_uuid_value_object import UserUUID
from app.domain.repositories.user_repository import UserRepositoryInterface
from app.infrastructure.database.postgres.models.user import UserModel
from app.infrastructure.database.postgres.repositories.common_repo import CommonSqlaRepo
from app.domain.exceptions.user_exceptions import UserNotFoundError, UserAlreadyExistsError
from app.infrastructure.database.postgres.mappers import user_model_to_entity, user_entity_to_model


class UserRepositoryImpl(CommonSqlaRepo, UserRepositoryInterface):
    async def get_user_by_uuid(self: Self, user_uuid: UserUUID) -> UserEntity:
        stmt = select(UserModel).where(UserModel.uuid == user_uuid.to_raw())
        result = await self.session.execute(statement=stmt)
        user: UserModel | None = result.scalars().first()
        if user is None:
            raise UserNotFoundError(f"User with uuid {user_uuid.to_raw()} not found")
        
        return user_model_to_entity(user=user)
    
    async def create_user(self: Self, user: UserEntity) -> UserUUID:
        user_db_model: UserModel = user_entity_to_model(user=user)
        stmt = insert(UserModel).values(user_db_model.to_dict()).returning(UserModel.uuid)
        try:
            result = await self.session.execute(statement=stmt)
            result: UUID = result.scalars().first()
        except IntegrityError:
            raise UserAlreadyExistsError(f'User with {user.user_contact.to_raw()} already exists')
        
        return UserUUID(result)
    
    async def delete_user(self: Self, user_uuid: UserUUID) -> None:
        stmt = delete(UserModel).where(UserModel.uuid == user_uuid.to_raw())
        try:
            await self.session.execute(statement=stmt)
        except IntegrityError:
            raise UserNotFoundError(f"User with uuid {user_uuid.to_raw()} not found")
        
    async def update_user_contact(
        self: Self, user_uuid: UserUUID, user_contact: UserContact, user_updated_at: UserUpdatedAt
    ) -> UserContact:
        stmt = update(UserModel).where(UserModel.uuid == user_uuid.to_raw()).values(
            user_contact=user_contact.to_raw(), user_updated_at=user_updated_at.to_raw()
        ).returning(UserModel.user_contact)
        try:
            result = await self.session.execute(statement=stmt)
            result: str = result.scalars().first()
        except IntegrityError:
            raise UserAlreadyExistsError(f'User with {user_contact.to_raw()} already exists')
        if result is None:
            raise UserNotFoundError(f"User with uuid {user_uuid.to_raw()} not found")
        
        return UserContact(result)
    
    async def update_user_name(
        self: Self, user_uuid: UserUUID, user_name: UserName, user_updated_at: UserUpdatedAt
    ) -> UserName:
        stmt = update(UserModel).where(UserModel.uuid == user_uuid.to_raw()).values(
            user_name=user_name.to_raw(), user_updated_at=user_updated_at.to_raw()
        ).returning(UserModel.user_name)
        result = await self.session.execute(statement=stmt)
        result: str = result.scalars().first()
        if result is None:
            raise UserNotFoundError(f"User with uuid {user_uuid.to_raw()} not found")

        return UserName(result)
    
    async def edit_user_status(self: Self, user_uuid: UserUUID, user_status: UserStatus) -> None:
        stmt = update(UserModel).where(UserModel.uuid == user_uuid.to_raw()).values(
            user_status=user_status.to_raw()
        )
        await self.session.execute(statement=stmt)

    async def get_user_uuid_by_contact(self: Self, user_contact: UserContact) -> UserUUID | None:
        stmt = select(UserModel.uuid).where(UserModel.user_contact == user_contact.to_raw())
        result = await self.session.execute(statement=stmt)
        result: UUID = result.scalars().first()
        if result is None:
            return None

        return UserUUID(result)


    

        

