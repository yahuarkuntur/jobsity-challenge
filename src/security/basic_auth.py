
import bcrypt
from datastore.redis_datastore import RedisDataStore
from settings import *


def check_password(username, password):
    key = 'chat:users:' + username
    redis = RedisDataStore()
    value = redis.get_value(key)

    if value is None:
        return False

    hashed = bcrypt.hashpw(password.encode('utf8'), CONFIG.get('server', 'password-salt'))

    if value == hashed:
        return True
    return False

# EOF
