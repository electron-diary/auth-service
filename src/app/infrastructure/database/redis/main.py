from redis.asyncio import RedisCluster
from redis.cluster import ClusterNode

from src.app.infrastructure.database.redis.config import RedisConfig


def redis_client(config: RedisConfig) -> RedisCluster:
    nodes: list[ClusterNode] = [ClusterNode(host=config.host, port=config.port)]
    redis: RedisCluster = RedisCluster(startup_nodes=nodes, decode_responses=True)
    return redis