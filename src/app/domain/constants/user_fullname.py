from dataclasses import dataclass
from typing import Self, Optional

from app.domain.value_objects.user_last_name_value_object import UserLastNameValueObject
from app.domain.value_objects.user_middle_name_value_object import UserMiddleNameValueObject
from app.domain.value_objects.user_first_name_value_object import UserFirstNameValueObject


@dataclass(frozen=True)
class UserFullName:
    user_first_name: UserFirstNameValueObject
    user_middle_name: UserMiddleNameValueObject
    user_last_name: UserLastNameValueObject

    