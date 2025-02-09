from src.settings import settings
from src.core.cache.redis import Redis


def get_cache() -> Redis:
    return Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
