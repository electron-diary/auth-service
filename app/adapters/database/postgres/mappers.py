from app.adapters.database.postgres.tables.user_table import UserTable
from app.application.dto.user_dto import UserDto


def convert_user_table_to_dto(user_table: UserTable) -> UserDto:
    user_dto: UserDto = UserDto(
        user_uuid=user_table.uuid,
        user_first_name=user_table.first_name,
        user_last_name=user_table.last_name,
        user_middle_name=user_table.middle_name,
        user_phone=user_table.user_phone,
        user_email=user_table.user_email,
    )
    return user_dto
