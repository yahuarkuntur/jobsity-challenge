
import bcrypt
from datastore.redis_datastore import RedisDataStore


def check_password(username, password):
    datastore = RedisDataStore()
    emisor_password = datastore.hget(username, 'password')
    emisor_salt = datastore.hget(username, 'salt')

    if emisor_password is None or emisor_salt is None:
        return False

    hashed = bcrypt.hashpw(password.encode('utf8'), emisor_salt)
    if hashed == emisor_password:
        return True
    return False

# EOF
