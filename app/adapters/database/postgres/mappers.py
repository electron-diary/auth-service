from app.adapters.database.postgres.tables.user_table import UserTable
from app.application.dto.user_dto import UserDto
from app.domain.events.create_user_event import CreateUserEvent


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

def convert_user_create_event_to_table(event: CreateUserEvent) -> UserTable:
    user_table: UserTable = UserTable(
        uuid=event.uuid,
        first_name=event.user_first_name,
        last_name=event.user_last_name,
        middle_name=event.user_middle_name,
        user_phone=event.user_phone,
        user_email=event.user_email,
    )
    return user_table
