from dishka import AsyncContainer, make_async_container

from src.app.main.dependency_injection.adapters.provide_nats_broker import NatsProvider
from src.app.main.dependency_injection.adapters.provide_sqla_db import SqlaProvider
from src.app.main.dependency_injection.usecases.provide_create_user_usecase import CreateUserUseCaseProvider
from src.app.main.dependency_injection.usecases.provide_delete_user_usecase import DeleteUserUseCaseProvider
from src.app.main.dependency_injection.usecases.provide_get_user_usecase import GetUserUseCaseProvider
from src.app.main.dependency_injection.usecases.provide_update_user_contact_usecase import UpdateUserContactUseCaseProvider
from src.app.main.dependency_injection.usecases.provide_update_user_name_usecase import UpdateUserNameUseCaseProvider
from src.app.main.dependency_injection.adapters.provide_configs import ConfigProvider
from src.app.main.dependency_injection.adapters.provide_user_name_generator import UserNameGeneratorProvider
from src.app.main.dependency_injection.usecases.provide_authentificate_user_usecase import AuthentificateeUserUseCaseProvider
from src.app.main.dependency_injection.usecases.provide_edit_user_status_usecase import EditUserStatusUseCaseProvider
from src.app.main.dependency_injection.adapters.provide_uuid_generator import UUIDGeneratorProvider
from src.app.main.dependency_injection.adapters.provide_mongo_db import MongoProvider
from src.app.main.dependency_injection.adapters.provide_redis_db import RedisProvider


def container_factory() -> AsyncContainer:
    container: AsyncContainer = make_async_container(
        MongoProvider(),
        RedisProvider(),
        UUIDGeneratorProvider(),
        UserNameGeneratorProvider(),
        EditUserStatusUseCaseProvider(),
        AuthentificateeUserUseCaseProvider(),
        ConfigProvider(),
        SqlaProvider(),
        NatsProvider(),
        CreateUserUseCaseProvider(),
        DeleteUserUseCaseProvider(),
        GetUserUseCaseProvider(),
        UpdateUserContactUseCaseProvider(),
        UpdateUserNameUseCaseProvider(),
    )
    return container