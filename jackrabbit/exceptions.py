

class ConeyException(Exception):
    def __repr__(self):
        return 'An unspecified error has occurred'


class CallTimeoutException(ConeyException):
    def __repr__(self):
        return 'An RPC call did not return before the time out period'


class MalformedRequestException(ConeyException):
    def __init__(self, serializer_name, request):
        self._serializer_name = serializer_name
        self._request = request

    def __repr__(self):
        return '{} failed to create a Request from string: {}'.format(self._serialier_name, self._request)


class RemoteExecErrorException(ConeyException):
    def __init__(self, value, details):
        self._value = value
        self._details = details

    def __repr__(self):
        return 'An error occurred during remote execution: ({}) {}'.format(self._value, self._details)

    @property
    def value(self):
        return self._value

    @property
    def details(self):
        return self._details


class RemoteUnhandledExceptionException(ConeyException):
    def __init__(self, details):
        self._details = details

    def __repr__(self):
        return 'An unhandled exception was raised during remote execution: {}'.format(self._details)


class DispatchHandlerException(ConeyException):
    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return 'Error {} occurred during message dispatch'.format(self.code)


class HandlerNotCallableException(ConeyException):
    def __repr__(self):
        return 'Handler provided a non-callable object'
