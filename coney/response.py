from .response_codes import ResponseCodes


class Response(object):
    def __init__(self, return_value, code=0, details={}):
        self._return_value = return_value
        self._code = code
        self._details = details

    @property
    def return_value(self):
        return self._return_value

    @property
    def code(self):
        return self._code

    @property
    def details(self):
        return self._details

    def __bool__(self):
        return self.code != 0

    # python 2.x version of __bool__
    __nonzero__ = __bool__

    @staticmethod
    def loads(s, serializer):
        try:
            l = serializer.loads(s)
        except (ValueError, TypeError):
            return Response(None, ResponseCodes.MALFORMED_RESPONSE, s)

        try:
            rv, code, details = l[0:3]
        except ValueError:
            return Response(None, ResponseCodes.MALFORMED_RESPONSE, s)
        else:
            return Response(rv, code, details)

    def dumps(self, serializer):
        return serializer.dumps([self.return_value, self.code, self.details])
