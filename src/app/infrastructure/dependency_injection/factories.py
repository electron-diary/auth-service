from dishka import AsyncContainer, make_async_container

from src.app.infrastructure.dependency_injection.adapters.provide_nats_broker import NatsProvider
from src.app.infrastructure.dependency_injection.adapters.provide_sqla_db import SqlaProvider
from src.app.infrastructure.dependency_injection.usecases.provide_create_user_usecase import CreateUserUseCaseProvider
from src.app.infrastructure.dependency_injection.usecases.provide_delete_user_usecase import DeleteUserUseCaseProvider
from src.app.infrastructure.dependency_injection.usecases.provide_get_user_usecase import GetUserUseCaseProvider
from src.app.infrastructure.dependency_injection.usecases.provide_update_user_contact_usecase import UpdateUserContactUseCaseProvider
from src.app.infrastructure.dependency_injection.usecases.provide_update_user_name_usecase import UpdateUserNameUseCaseProvider


def container_factory() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        SqlaProvider(),
        NatsProvider(),
        CreateUserUseCaseProvider(),
        DeleteUserUseCaseProvider(),
        GetUserUseCaseProvider(),
        UpdateUserContactUseCaseProvider(),
        UpdateUserNameUseCaseProvider(),
    )
    return container