import logging
import pika
import traceback
import uuid

import constants
from .compressors.null_compressor import NullCompressor
from .exceptions import CallTimeoutException, RemoteUnhandledExceptionException
from .request import Request
from .response import Response
from .response_codes import ResponseCodes
from .serializers.msgpack_serializer import MsgpackSerializer

logger = logging.getLogger(__name__)


class ProxyBase(object):
    def __init__(self, uri, call_timeout=30, serializer=MsgpackSerializer, compressor=NullCompressor,
                 reraise_remote_exceptions=False):
        self._uri = uri
        self._serializer = serializer
        self._compressor = compressor
        self._reraise_remote_exceptions = reraise_remote_exceptions

        params = pika.URLParameters(uri)

        self._conn_params = params
        self._connect()

        self._correlation_id = None
        self._response = None

    def _connect(self):
        self._connection = pika.BlockingConnection(parameters=self._conn_params)
        self._channel = self._connection.channel()
        self._channel.basic_consume(self._response, no_ack=True, queue=constants.RABBITMQ_REPLYTO_QUEUE)

    def _response(self, ch, meth, props, body):
        if props.correlation_id == self._correlation_id:
            self._response = body

    def _call(self, method, data):
        self._correlation_id = str(uuid.uuid4())
        self._response = None

        compressed_value = self._compressor.compress(data)

        tries_remaining = 2
        while tries_remaining:
            tries_remaining -= 1
            try:
                self._channel.basic_publish(
                    exchange='',
                    routing_key=method,
                    properties=pika.BasicProperties(
                        reply_to=constants.RABBITMQ_REPLYTO_QUEUE,
                        correlation_id=self._correlation_id
                    ),
                    body=compressed_value
                )
                tries_remaining = 0
            except pika.exceptions.ConnectionClosed:
                if tries_remaining:
                    logger.info('Connection to queue was closed, reconnecting')
                    self._connect()
                else:
                    logger.error('Reconnect failed: {}'.format(traceback.format_exc(limit=10)))
                    raise

        sleep_interval_seconds = 0.1
        while not self._response:
            # implement timeout check here
            # if timeout: raise CallTimeoutException
            self._connection.sleep(sleep_interval_seconds)

        # Pull the response out and return it
        return self._compressor.decompress(self._response)

    @staticmethod
    def generate_metadata():
        return {}

    def exec_rpc(self, method, version, **kwargs):
        metadata = self.generate_metadata()
        request = Request(version, metadata, kwargs)
        try:
            str_request = request.dumps(self._serializer)
        except ValueError as ex:
            logger.error("Encoding error while serializing request: {}".format(request))
            return Response(None, ResponseCodes.REQUEST_ENCODING_FAILURE, ex)

        try:
            str_response = self._call(method, str_request)
        except CallTimeoutException:
            logger.warn("exec_rpc timeout: method={}, version={}, args={}".format(method, version, kwargs))
            response = Response(None, ResponseCodes.CALL_REPLY_TIMEOUT)
        else:
            # Decode response and return
            response = Response.loads(str_response, self._serializer)

        if self._reraise_remote_exceptions and response.code == ResponseCodes.REMOTE_UNHANDLED_EXCEPTION:
            raise RemoteUnhandledExceptionException(response.details)

        return response
