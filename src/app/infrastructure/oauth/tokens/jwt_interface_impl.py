from typing import Self
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import PyJWTError

from src.app.domain.user.value_objects import UserUUID
from src.app.infrastructure.oauth.tokens.jwt_interface import JwtTokenInterface
from src.app.domain.common.exceptions import AuthentificationError


class JwtTokenService(JwtTokenInterface):
    def __init__(self: Self, config: ...) -> None:
        self.config: ... = config

    def encode_access_token(self: Self, user_id: UserUUID) -> str:
        to_encode_access_data: dict[str] = dict(
            sub = str(user_id),
            token_type = 'access',
            iat = datetime.now(),
            exp = datetime.now() + timedelta(minutes=self.config.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        return jwt.encode(
            payload=to_encode_access_data,
            key=self.config.SECRET_KEY,
            algorithm=self.config.ALGORITHM
        )

    def encode_refresh_token(self: Self, user_id: UserUUID) -> str:
        to_encode_refresh_data: dict[str] = dict(
            sub = str(user_id),
            token_type = 'refresh',
            iat = datetime.now(),
            exp = datetime.now() + timedelta(days=self.config.REFRESH_TOKEN_EXPIRE_DAYS)
        )
        return jwt.encode(
            payload=to_encode_refresh_data,
            key=self.config.SECRET_KEY,
            algorithm=self.config.ALGORITHM
        )
        
    def decode_token(self: Self, token: str) -> dict[str]:
        try:
            payload: dict[str] = jwt.decode(
                jwt=token,
                key=self.config.PUBLIC_KEY,
                algorithms=[self.config.ALGORITHM]
            )
            return payload
        except PyJWTError:
            raise AuthentificationError('Invalid token')
        
    def get_user_uuid_from_token(self: Self, token: str) -> UserUUID:
        try:
            payload: dict[str] = self.decode_token(token=token)
        except PyJWTError:
            raise AuthentificationError('Invalid token')

        try:
            user_uuid: UserUUID = UserUUID(payload['sub'])
            return user_uuid
        except KeyError:
            raise AuthentificationError('Invalid token')

    def update_access_token(self: Self, refresh_token: str) -> str:
        try:
            payload: dict[str] = self.decode_token(token=refresh_token)
        except PyJWTError:
            raise AuthentificationError('Invalid token')

        try: 
            if payload['token_type'] != 'refresh':
                raise AuthentificationError('Invalid token')
        except KeyError:
            raise AuthentificationError('Invalid token')

        return self.encode_access_token(
            user_id=str(self.get_user_uuid_from_token(token=refresh_token))
        )
        