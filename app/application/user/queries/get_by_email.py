from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserByEmailQuery:
    email: str
