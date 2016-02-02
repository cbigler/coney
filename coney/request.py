from .exceptions import MalformedRequestException


class Request(object):
    def __init__(self, version, metadata, **kwargs):
        self._version = version
        self._metadata = metadata
        self._arguments = kwargs

    @property
    def version(self):
        return self._version

    @property
    def arguments(self):
        return self._arguments

    @property
    def metadata(self):
        return self._metadata

    @staticmethod
    def loads(s, serializer):
        try:
            l = serializer.loads(s)
        except(ValueError, TypeError):
            raise MalformedRequestException(serializer.__name__, s)

        try:
            version, metadata, args = l[0:3]
        except ValueError:
            raise MalformedRequestException(serializer.__name__, s)
        else:
            return Request(version, metadata, args)

    @staticmethod
    def dumps(obj, serializer):
        return serializer.dumps([obj.version, obj.metadata, obj.arguments])

