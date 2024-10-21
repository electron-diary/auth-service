from typing import Self
import jwt
from jwt.exceptions import PyJWTError
from datetime import datetime, timedelta

from src.app.domain.value_objects.user_status_value_object import UserStatus
from src.app.domain.value_objects.user_uuid_value_object import UserUUID
from src.app.infrastructure.authentification.web.tokens.repository_interface import JwtRepositoryInterface
from src.app.infrastructure.authentification.web.config import AuthConfig
from src.app.infrastructure.authentification.web.tokens.constants import UserData, TokenData
from src.app.application.exceptions.auth_exceptions import AuthentificationError


class JwtRepository(JwtRepositoryInterface):
    def __init__(self: Self, config: AuthConfig) -> None:
        self.config: AuthConfig = config

    def decode_token(self: Self, token: str | bytes) -> UserData:
        try:
            payload: dict[str] = jwt.decode(
                jwt=token, key = self.config.public_key, algorithms=[self.config.algorithm]
            )
        except PyJWTError:
            raise AuthentificationError('authentification error')
        
        try:
            user_uuid: UserUUID = UserUUID(payload['sub'])
            user_status: UserStatus = UserStatus(payload['status'])
            
            return UserData(user_uuid=user_uuid, user_status=user_status)
        except ValueError:
            raise AuthentificationError('authentification error')
        
    def encode_access_token(self: Self, user_data: UserData) -> TokenData:
        access_expires_at: datetime = datetime.now() + timedelta(minutes=self.config.access_expire_minutes)
        to_encode: dict[str] = dict(
            sub = UserUUID(user_data.user_uuid).to_raw(),
            expires_at = access_expires_at,
            status = UserStatus(user_data.status).to_raw(),
            type = 'access'
        )
        token: str | bytes = jwt.encode(
            payload=to_encode, key=self.config.secret_key.read_text(), algorithm=self.config.algorithm
        )
        return TokenData(token=token, expires_at=access_expires_at)
    
    def encode_refresh_token(self: Self, user_data: UserData) -> TokenData:
        refresh_expires_at: datetime = datetime.now() + timedelta(days=self.config.refresh_expire_days)
        to_encode: dict[str] = dict(
            sub = UserUUID(user_data.user_uuid).to_raw(),
            expires_at = refresh_expires_at,
            status = UserStatus(user_data.status).to_raw(),
            type = 'refresh'
        )
        token: str | bytes = jwt.encode(
            payload=to_encode, key=self.config.secret_key.read_text(), algorithm=self.config.algorithm
        )
        return TokenData(token=token, expires_at=refresh_expires_at)
        

    def update_access_token(self: Self, refresh_token: TokenData) -> TokenData:
        if refresh_token.expires_at <= datetime.now():
            raise AuthentificationError('authentification error')
        refresh_token_data: dict[str] = self.decode_token(token=refresh_token.token)
        return self.encode_access_token(
            user_data=refresh_token_data
        )

