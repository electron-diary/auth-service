from typing import Self
from dataclasses import dataclass
from uuid import UUID
import ipaddress
from datetime import datetime
import base64

from src.app.domain.common.value_objects import DomainValueObject
from src.app.domain.common.exceptions import DomainValidationError


@dataclass(frozen=True)
class UserUUID(DomainValueObject[UUID]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User UUID cannot be empty"
            )
        if not isinstance(self.object, UUID):
            raise DomainValidationError(
                "User UUID must be a valid UUID"
            )
        
@dataclass(frozen=True)
class UserName(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User name cannot be empty"
            )
        if not isinstance(self.object, str):
            raise DomainValidationError(
                "User name must be a string"
            )
        if len(self.object) < 3:
            raise DomainValidationError(
                "User name must be at least 3 characters long"
            )
        if len(self.object) > 20:
            raise DomainValidationError(
                "User name must be less than 50 characters long"
            )
        
@dataclass(frozen=True)
class UserContact(DomainValueObject[str | int]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User contact cannot be empty"
            )
        if not isinstance(self.object, (str, int)):
            raise DomainValidationError(
                "User contact must be a string or an integer"
            )
        if isinstance(self.object, str) and len(self.object) > 20:
            raise DomainValidationError(
                "User contact must be less than 20 characters long"
            )
        
@dataclass(frozen=True)
class UserPassword(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User password cannot be empty"
            )
        if not isinstance(self.object, str):
            raise DomainValidationError(
                "User password must be a string"
            )
        if len(self.object) < 8:
            raise DomainValidationError(
                "User password must be at least 8 characters long"
            )
        if len(self.object) > 20:
            raise DomainValidationError(
                "User password must be less than 20 characters long"
            )
    
@dataclass(frozen=True)
class UserIp(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User IP cannot be empty"
            )
        if not isinstance(self.object, str):
            raise DomainValidationError(
                "User IP must be a string"
            )

        if not ipaddress.ip_address(self.object):
            raise DomainValidationError(
                "User IP must be a valid IP address"
            )
        
@dataclass(frozen=True)
class UserCreatedAt(DomainValueObject[datetime]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User created at cannot be empty"
            )
        if not isinstance(self.object, datetime):
            raise DomainValidationError(
                "User created at must be a datetime"
            )
        
@dataclass(frozen=True)
class UserCreatedAt(DomainValueObject[datetime]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User created at cannot be empty"
            )
        if not isinstance(self.object, datetime):
            raise DomainValidationError(
                "User created at must be a datetime"
            )
    
@dataclass(frozen=True)
class UserUpdatedAt(DomainValueObject[datetime]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User updated at cannot be empty"
            )
        if not isinstance(self.object, datetime):
            raise DomainValidationError(
                "User updated at must be a datetime"
            )
        
@dataclass(frozen=True)
class UserRefreshToken(DomainValueObject[str]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User refresh token cannot be empty"
            )
        if not isinstance(self.object, str):
            raise DomainValidationError(
                "User refresh token must be a string"
            )
        if not base64.decode(self.object):
            raise DomainValidationError(
                "User refresh token must be a valid base64 string"
            )
        if len(self.object.split('.')) != 3:
            raise DomainValidationError(
                "User refresh token must be a valid JWT token"
            )
        
@dataclass(frozen=True)
class UserStatus(DomainValueObject[bool]):
    def validate(self: Self) -> None:
        if not self.object:
            raise DomainValidationError(
                "User status cannot be empty"
            )
        if not isinstance(self.object, bool):
            raise DomainValidationError(
                "User status must be a string"
            )

        

        
