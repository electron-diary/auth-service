from dataclasses import dataclass


@dataclass(frozen=True)
class GetUserByPhoneQuery:
    phone: int
