"""
Redis class to handle all the redis operations
"""

import redis


class Redis:
    """
    Redis class to handle all the redis operations
    """

    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db

    def get_connection(self):
        return redis.Redis(host=self.host, port=self.port, db=self.db)

    def set(self, key, value, expiration):
        self.get_connection().setex(key, expiration, value)

    def get(self, key):
        return self.get_connection().get(key)
