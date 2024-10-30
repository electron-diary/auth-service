from redis.asyncio import RedisCluster
from redis.cluster import ClusterNode
import logging
from logging import Logger

from src.app.infrastructure.database.redis.config import RedisConfig


logger: Logger = logging.getLogger(__name__)


def redis_client(config: RedisConfig) -> RedisCluster:
    nodes: list[ClusterNode] = [ClusterNode(host=config.host, port=config.port)]
    redis: RedisCluster = RedisCluster(startup_nodes=nodes, decode_responses=True)
    logger.info('connected to redis')
    return redis