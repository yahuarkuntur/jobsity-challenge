#!/usr/bin/env python

import json
import bottle
import time
import os
import sys
from bottle import route, error, request, response, static_file, auth_basic
from datastore.redis_datastore import RedisDataStore
from security.cors import EnableCors
from security.basic_auth import check_password
from rabbitmq.producer import RabbitMQProducer
from settings import *

reload(sys)
sys.setdefaultencoding('utf8')


@error(404)
@error(401)
@error(400)
@error(500)
def errorXXX(err):
    response.headers['Content-type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = CONFIG.get('server', 'allow-origin')
    return json.dumps({
        'error': {
            'http_code': err.status_code,
            'message': err.body
        }
    })


@route('/api/chatrooms', method=['OPTIONS', 'GET'])
def list_chatrooms():
    response.headers['Content-type'] = 'application/json'
    return json.dumps(['Default', 'Development', 'DevOps', 'Databases'])


@route('/api/chatrooms/<chatroom_id>/messages', method=['OPTIONS', 'GET'])
def get_messages(chatroom_id):
    response.headers['Content-type'] = 'application/json'
    redis = RedisDataStore()
    key = 'chat:' + chatroom_id.lower() + ':messages'
    messages = redis.lrange(key, 0, 50)
    return json.dumps(messages)


@route('/api/chatrooms/<chatroom_id>/messages', method=['OPTIONS', 'POST'])
def new_message(chatroom_id):
    response.headers['Content-type'] = 'application/json'
    obj = request.json
    payload = {
        'm': obj['m'],
        't': time.time(),
        'r': str(chatroom_id),
        'u': request.auth[0],
    }
    value = json.dumps(payload)
    key = 'chat:' + chatroom_id.lower() + ':messages'
    redis = RedisDataStore()
    redis.rpush(key, value)
    producer = RabbitMQProducer('commands')
    producer.queue(value)
    producer.stop()
    return value


@route('/fonts/<filename>')
def serve_static_fonts(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static', 'fonts'))


@route('/css/<filename>')
def serve_static_css(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static', 'css'))


@route('/js/<filename>')
def serve_static_js(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static', 'js'))


@route('/')
@auth_basic(check_password)
def app_homepage(filename='index.html'):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static'))


if __name__ == '__main__':
    host = CONFIG.get('server', 'host')
    port = int(CONFIG.get('server', 'port'))
    app = bottle.app()
    app.install(EnableCors())
    app.run(host=host, port=port, debug=True, server='paste')


# EOF
