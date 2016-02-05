from json import loads, dumps, JSONEncoder


class _JsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, set):
            return list(o)

        return JSONEncoder.default(self, o)


class JsonSerializer(object):
    @staticmethod
    def dumps(o):
        return dumps(o, cls=_JsonEncoder)

    @staticmethod
    def loads(s):
        return loads(s)
