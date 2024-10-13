from typing import Self
from uuid import UUID
from sqlalchemy import select, update, delete, insert
from sqlalchemy.exc import IntegrityError

from src.app.domain.user.entity import UserEntity
from src.app.domain.user.repositories import UserInterface
from src.app.domain.user.value_objects import UserContact, UserCreatedAt, UserUUID, UserName, UserUpdatedAt
from src.app.infrastructure.database.postgres.models.user import UserModel
from src.app.infrastructure.database.postgres.repositories.common_repo import CommonSqlaRepo
from src.app.domain.user.exceptions import UserNotFoundError, UserAlreadyExistsError
from src.app.infrastructure.database.postgres.mappers import user_model_to_entity


class UserRepositoryImpl(CommonSqlaRepo, UserInterface):
    async def get_user_by_uuid(self: Self, user_uuid: UserUUID) -> UserEntity:
        stmt = select(UserModel).where(UserModel.uuid == user_uuid.to_raw())
        result = await self.session.execute(statement=stmt)
        user: UserModel | None = result.scalars().first()
        if user is None:
            raise UserNotFoundError(f"User with uuid {user_uuid.to_raw()} not found")
        
        return user_model_to_entity(user=user)
    
    async def create_user(
        self: Self, user_name: UserName, user_contact: UserContact, 
        user_created_at: UserCreatedAt, user_updated_at: UserUpdatedAt,
    ) -> UserUUID:
        stmt = insert(UserModel).values(
            user_name=user_name.to_raw(), user_contact=user_contact.to_raw(), 
            user_created_at=user_created_at.to_raw(), user_updated_at=user_updated_at.to_raw()
        ).returning(UserModel.uuid)
        try:
            result = await self.session.execute(statement=stmt)
            result: UUID = result.scalars().first()
        except IntegrityError:
            raise UserAlreadyExistsError(f'User with {user_contact.to_raw()} already exists')
        
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


    

        

