#!/usr/bin/env python

import logging
import json
import time
from rabbitmq.consumer import RabbitMQConsumer
from datastore.redis_datastore import RedisDataStore
from chatbot.webservice import Webservice
from chatbot.command_parser import CommandParser
from settings import *

LOGGER = logging.getLogger(__name__)


class Consumer(RabbitMQConsumer):

    def __init__(self, queue):
        RabbitMQConsumer.__init__(self, queue)

    def callback(self, ch, method, properties, body):
        # get message
        payload = json.loads(body)
        chatroom = payload['r']
        message = payload['m']

        # ack message
        super(Consumer, self).callback(ch, method, properties, body)

        parser = CommandParser()
        command = parser.parse(message)

        if command == 'help':
            response = 'Type /stock=stock_code to get stock quote.'
        elif command is None:
            response = 'The command is invalid.'
        else:
            webservice = Webservice(command)
            response = webservice.call()

        payload = {
            'u': 'Chatbot',
            'm': response,
            't': time.time(),
            'r': chatroom
        }
        value = json.dumps(payload)
        key = 'chat:' + chatroom.lower() + ':messages'
        redis = RedisDataStore()
        redis.rpush(key, value)


if __name__ == '__main__':
    consumer = Consumer('commands')

    try:
        consumer.run()
    except KeyboardInterrupt:
        LOGGER.warning('Closing worker by SIGINT')
        consumer.stop()

# EOF
