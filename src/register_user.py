#!/usr/bin/env python

import logging
import bcrypt
from datastore.redis_datastore import RedisDataStore
from settings import *


if __name__ == '__main__':
    username = raw_input('New username: ')
    password = raw_input('New password: ')

    key = 'chat:users:' + username
    redis = RedisDataStore()
    value = redis.get_value(key)

    if value is None:
        hashed = bcrypt.hashpw(password.encode('utf8'), CONFIG.get('server', 'password-salt'))
        redis.set_value(key, hashed)
    else:
        print username, 'already exists.'

# EOF
