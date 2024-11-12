from enum import IntEnum


class UserFullnameEnums(IntEnum):
    user_middle_name_max_lenght: int = 50
    user_first_name_max_length: int = 50
    user_last_name_max_length: int = 50
    user_first_name_min_length: int = 2
    user_last_name_min_length: int = 2
    user_middle_name_min_length: int = 2
