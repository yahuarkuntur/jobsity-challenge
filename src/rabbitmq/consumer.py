
import json
import pika
from base_rabbitmq import BaseRabbitMQ


class RabbitMQConsumer(BaseRabbitMQ):

    def __init__(self, queue):
        self._queue = queue
        self._exchange = queue + '_exchange'
        BaseRabbitMQ.__init__(self)

        self.channel.queue_declare(queue=self._queue, durable=True)
        self.channel.basic_qos(prefetch_count=1)
        self.channel.exchange_declare(
            exchange=self._exchange,
            exchange_type='direct',
            durable=True
        )
        self.channel.queue_bind(
            exchange=self._exchange,
            queue=self._queue
        )

    def run(self):
        self.channel.basic_consume(self.callback, queue=self._queue)
        self.channel.start_consuming()

    def queue(self, message):
        self.channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._queue,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            )
        )

    # Metodo para procesar el mensaje
    def callback(self, ch, method, properties, body):
        # send ACK = remove message from the queue
        ch.basic_ack(delivery_tag=method.delivery_tag)

# EOF
