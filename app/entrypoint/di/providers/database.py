from collections.abc import AsyncGenerator

from dishka import AnyOf, Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine

from app.application.common.profile_reader import ProfileReader
from app.application.common.unit_of_work import UnitOfWork, UnitOfWorkCommitter
from app.application.common.user_reader import UserReader
from app.domain.profile.entities.address import Address
from app.domain.profile.entities.profile import Profile
from app.domain.profile.entities.social_netw_profile import SocialNetwProfile
from app.domain.profile.repositories.profile_repository import ProfileRepository
from app.domain.user.entities.user import User
from app.domain.user.repositories.user_repository import UserRepository
from app.infrastructure.database.postgres.config import PostgresConfig
from app.infrastructure.database.postgres.gateways.address_data_mapper import AddressDataMapper
from app.infrastructure.database.postgres.gateways.profile_data_mapper import ProfileDataMapper
from app.infrastructure.database.postgres.gateways.profile_reader import ProfileReaderImpl
from app.infrastructure.database.postgres.gateways.profile_repository import ProfileRepositoryImpl
from app.infrastructure.database.postgres.gateways.social_netw_profile_data_mapper import SocialNetwProfileDataMapper
from app.infrastructure.database.postgres.gateways.user_data_mapper import UserDataMapper
from app.infrastructure.database.postgres.gateways.user_reader import UserReaderImpl
from app.infrastructure.database.postgres.gateways.user_repository import UserRepositoryImpl
from app.infrastructure.database.postgres.interfaces.registry import Registry
from app.infrastructure.database.postgres.main import postgres_engine
from app.infrastructure.database.postgres.registry import RegistryImpl
from app.infrastructure.database.postgres.unit_of_work import UnitOfWorkImpl


class PostgresDatabaseProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_postgres_config(self) -> PostgresConfig:
        return PostgresConfig()

    @provide(scope=Scope.APP)
    def provide_postgres_engine(
        self,
        config: PostgresConfig,
    ) -> AsyncEngine:
        return postgres_engine(config)

    @provide(scope=Scope.REQUEST, provides=AsyncConnection)
    async def provide_postgres_connection(
        self,
        engine: AsyncEngine,
    ) -> AsyncGenerator[AsyncConnection, None]:
        async with engine.begin() as connection:
            yield connection

    @provide(scope=Scope.REQUEST)
    def provide_user_repository(
        self,
        connection: AsyncConnection,
        unit_of_work: UnitOfWork,
    ) -> UserRepository:
        return UserRepositoryImpl(connection, unit_of_work)

    @provide(scope=Scope.REQUEST)
    def provide_profile_repository(
        self,
        connection: AsyncConnection,
        unit_of_work: UnitOfWork,
    ) -> ProfileRepository:
        return ProfileRepositoryImpl(unit_of_work, connection)

    @provide(scope=Scope.REQUEST)
    def provide_user_reader(
        self,
        connection: AsyncConnection,
    ) -> UserReader:
        return UserReaderImpl(connection)

    @provide(scope=Scope.REQUEST)
    def provide_profile_reader(
        self,
        connection: AsyncConnection,
    ) -> ProfileReader:
        return ProfileReaderImpl(connection)

    @provide(scope=Scope.REQUEST)
    def provide_user_data_mapper(
        self,
        connection: AsyncConnection,
    ) -> UserDataMapper:
        return UserDataMapper(connection)

    @provide(scope=Scope.REQUEST)
    def provide_profile_data_mapper(
        self,
        connection: AsyncConnection,
    ) -> ProfileDataMapper:
        return ProfileDataMapper(connection)

    @provide(scope=Scope.REQUEST)
    def provide_address_data_mapper(
        self,
        connection: AsyncConnection,
    ) -> AddressDataMapper:
        return AddressDataMapper(connection)

    @provide(scope=Scope.REQUEST)
    def provide_social_netw_profile_data_mapper(
        self,
        connection: AsyncConnection,
    ) -> SocialNetwProfileDataMapper:
        return SocialNetwProfileDataMapper(connection)

    @provide(scope=Scope.REQUEST)
    def provide_registry(
        self,
        address_data_mapper: AddressDataMapper,
        profile_data_mapper: ProfileDataMapper,
        social_netw_profile_data_mapper: SocialNetwProfileDataMapper,
        user_data_mapper: UserDataMapper,
    ) -> Registry:
        registry = RegistryImpl()
        registry.register_mapper(Address, address_data_mapper)
        registry.register_mapper(Profile, profile_data_mapper)
        registry.register_mapper(SocialNetwProfile, social_netw_profile_data_mapper)
        registry.register_mapper(User, user_data_mapper)
        return registry

    @provide(scope=Scope.REQUEST)
    def provide_unit_of_work(
        self,
        connection: AsyncConnection,
        registry: Registry,
    ) -> AnyOf[UnitOfWorkCommitter, UnitOfWork]:
        return UnitOfWorkImpl(registry, connection)
