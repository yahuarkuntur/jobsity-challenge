
import pika
import os
from settings import *


class BaseRabbitMQ(object):

    def __init__(self):
        credentials = pika.PlainCredentials(
            CONFIG.get('rabbitmq', 'username'),
            CONFIG.get('rabbitmq', 'password')
        )
        parameters = pika.ConnectionParameters(
            credentials=credentials,
            host=CONFIG.get('rabbitmq', 'host'),
            port=int(CONFIG.get('rabbitmq', 'port')),
            virtual_host=str(CONFIG.get('rabbitmq', 'vhost'))
        )
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def stop(self):
        self.channel.stop_consuming()

# EOF
