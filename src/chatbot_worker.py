#!/usr/bin/env python

import logging
import json
from rabbitmq.consumer import RabbitMQConsumer
from settings import *

LOGGER = logging.getLogger(__name__)


class Consumer(RabbitMQConsumer):

    def __init__(self, queue):
        RabbitMQConsumer.__init__(self, queue)

    def callback(self, ch, method, properties, body):
        # get message
        message = json.loads(body)

        # ack message
        super(Consumer, self).callback(ch, method, properties, body)

        # TODO process command
        # post response to chatroom
        # post error to chatroom
        # {"m":"Hello World!","t":1436263599489,"u":"Brian","r":"Tech"}



if __name__ == '__main__':
    consumer = Consumer('chatbot_commands')

    try:
        consumer.run()
    except KeyboardInterrupt:
        LOGGER.warning('Closing worker by SIGINT')
        consumer.stop()

# EOF
