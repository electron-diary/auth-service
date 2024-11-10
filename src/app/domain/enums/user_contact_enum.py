from enum import Enum


class UserContactEnums(Enum):
    user_phone_max_lenght: int = 20
    user_email_max_lenght: int  = 250
    user_phone_min_lenght: int  = 10
    user_email_min_lenght: int = 5
