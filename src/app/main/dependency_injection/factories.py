from dishka import AsyncContainer, make_async_container

from app.main.dependency_injection.adapters.provide_nats_broker import NatsProvider
from app.main.dependency_injection.adapters.provide_sqla_db import SqlaProvider
from app.main.dependency_injection.usecases.provide_create_user_usecase import CreateUserUseCaseProvider
from app.main.dependency_injection.usecases.provide_delete_user_usecase import DeleteUserUseCaseProvider
from app.main.dependency_injection.usecases.provide_get_user_usecase import GetUserUseCaseProvider
from app.main.dependency_injection.usecases.provide_update_user_contact_usecase import UpdateUserContactUseCaseProvider
from app.main.dependency_injection.usecases.provide_update_user_name_usecase import UpdateUserNameUseCaseProvider
from app.main.dependency_injection.adapters.provide_configs import ConfigProvider
from app.main.dependency_injection.adapters.provide_user_name_generator import UserNameGeneratorProvider
from app.main.dependency_injection.usecases.provide_authentificate_user_usecase import AuthentificateeUserUseCaseProvider
from app.main.dependency_injection.usecases.provide_edit_user_status_usecase import EditUserStatusUseCaseProvider
from app.main.dependency_injection.adapters.provide_uuid_generator import UUIDGeneratorProvider
from app.main.dependency_injection.adapters.provide_mongo_db import MongoProvider
from app.main.dependency_injection.adapters.provide_redis_db import RedisProvider


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