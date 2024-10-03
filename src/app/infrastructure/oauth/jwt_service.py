from typing import Self
from datetime import datetime, timedelta
import jwt

from app.domain.user.value_objects import UserUUID
from src.app.infrastructure.oauth.jwt_interface import JwtTokenInterface


class JwtTokenService(JwtTokenInterface):
    def __init__(self: Self) -> None:
        pass

    def decode_token(self: Self, token: str) -> UserUUID:
        pass

    def encode_token(self: Self, payload: dict[UserUUID]) -> str:
        pass

    def validate_token(self: Self, token: str) -> bool:
        pass