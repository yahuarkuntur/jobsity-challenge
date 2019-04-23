#!/usr/bin/env python

import json
import bottle
import os
import sys
from bottle import route, error, request, response, run, static_file, BaseRequest, hook
#from security.token_auth import *
from security.cors import EnableCors
#from controllers.static import StaticController
from settings import *

reload(sys)
sys.setdefaultencoding('utf8')
BaseRequest.MEMFILE_MAX = 2 * 1024 * 1024

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


# Chat rooms
@route('/api/chatrooms', method=['OPTIONS', 'GET'])
def list_chatrooms():
    response.headers['Content-type'] = 'application/json'
    # TODO return number of users?
    return json.dumps(
        [ 'One', 'Two', 'Tree' ]
    )

@route('/api/chatrooms', method=['OPTIONS', 'POST'])
def create_chatroom():
    response.headers['Content-type'] = 'application/json'
    # TODO check chatroom does not exist
    return json.dumps(
        [ 'One', 'Two', 'Tree' ]
    )


#@route('/api/chatrooms/<chatroom_id>/messages', method=['OPTIONS', 'GET'])
#def get_messages(chatroom_id):
#    response.headers['Content-type'] = 'application/json'
#    return json.dumps(
#        [ 'Hello', 'World' ]
#    )


@route('/api/chatrooms/<chatroom_id>/join', method=['OPTIONS', 'GET'])
def get_messages(chatroom_id):
    response.headers['Content-type'] = 'application/json'
    # TODO return 50 latest messages
    return json.dumps(
        [ 'Hello', 'World' ]
    )


#@route('/static/comprobantes/<comprobante_id>', method='GET')
#def static_comprobante_from_id(comprobante_id):
#    return StaticController.comprobante_from_id(comprobante_id)

@route('/css/<filename>')
def serve_static_css(filename):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static', 'css'))

@route('/')
def app_homepage(filename='index.html'):
    return static_file(filename, root=os.path.join(ROOT_DIR, 'static'))


if __name__ == '__main__':
    host = CONFIG.get('server', 'host')
    port = int(CONFIG.get('server', 'port'))
    app = bottle.app()
    app.install(EnableCors())
    app.run(host=host, port=port, debug=True, server='paste')


# EOF
