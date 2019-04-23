
import redis
import os
from settings import *


class RedisDataStore:

    def __init__(self):
        self.conn = redis.Redis(
            host=CONFIG.get('redis', 'host'),
            port=CONFIG.get('redis', 'port')
        )

    def get_value(self, key):
        return self.conn.get(key)

    def set_value(self, key, value):
        self.conn.set(key, value)

    def get_keys(self, key):
        return self.conn.keys(key)

    def delete_key(self, key):
        self.conn.delete(key)

    def decrement(self, key, amount=1):
        self.conn.decr(key, amount)

    def hget(self, key, field):
        return self.conn.hget(key, field)

    def hset(self, key, field, value):
        self.conn.hset(key, field, value)
