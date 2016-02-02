import pika
import uuid

import constants


class NamedQueueRoutingStrategy(object):
    """
    named queue routing strategy relies on a named-queue per endpoint, usually partitioned
    by vhosts. RPC calls are routed to their handlers
    """

    def __init__(self, channel, exchange=''):
        self._channel = channel
        self._exchange = exchange

    def publish(self, method, data):
        correlation_id = str(uuid.uuid4())

        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=method,
            properties=pika.BasicProperties(
                reply_to=constants.RABBITMQ_REPLYTO_QUEUE,
                correlation_id=correlation_id
            ),
            body=data
        )

        return correlation_id
