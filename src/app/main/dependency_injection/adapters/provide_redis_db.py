from typing import Self, AsyncGenerator
from dishka import Provider, provide, Scope
from redis.asyncio import RedisCluster, Redis

from src.app.main.config import ConfigFactory
from src.app.infrastructure.database.redis.config import RedisConfig
from src.app.infrastructure.database.redis.main import redis_client


class RedisProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_redis_config(self: Self, config: ConfigFactory) -> RedisConfig:
        return config.redis_config
    
    @provide(scope=Scope.APP)
    def provide_redis_cluster(self: Self, config: RedisConfig) -> RedisCluster:
        return redis_client(config = config)
    
    @provide(scope=Scope.REQUEST, provides=Redis)
    async def provide_redis(self: Self, redis: RedisCluster) -> AsyncGenerator[Redis, None]:
        try:
            yield redis
            await redis.close()
        finally:
            await redis.close()