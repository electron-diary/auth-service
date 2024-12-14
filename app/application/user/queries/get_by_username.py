from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserByUsernameQuery:
    username: str