from typing import Self
from uuid import UUID
from datetime import datetime

from src.app.domain.user.entity import UserEntity
from src.app.domain.user.value_objects import UserUUID
from src.app.domain.user.value_objects import UserName
from src.app.domain.user.value_objects import UserContact
from src.app.domain.user.value_objects import UserCreatedAt
from src.app.domain.user.value_objects import UserUpdatedAt
from src.app.application.dto.auth.request_dto import LoginUserDto, RegisterUserDto
from app.application.interfaces.interactor import Interactor
from src.app.domain.user.repositories import UserInterface

